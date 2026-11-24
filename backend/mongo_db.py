"""
AlgoForge MongoDB Atlas Integration Module
Provides document storage for user accounts, credentials, telemetry, submissions, and audit logs.
Features automatic DNS SRV resolution, credential validation, auto-seeding, and seamless fallback.
"""

import os
import json
import time
import urllib.parse
from datetime import datetime
from typing import Optional, List, Dict, Any

# Ensure public DNS resolution for MongoDB Atlas SRV records
try:
    import dns.resolver
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '1.1.1.1', '8.8.4.4']
    resolver.timeout = 3.0
    resolver.lifetime = 3.0
    dns.resolver.default_resolver = resolver
except Exception:
    pass

try:
    import pymongo
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError
    PYMONGO_AVAILABLE = True
except ImportError:
    PYMONGO_AVAILABLE = False

DEFAULT_MONGO_URI_TEMPLATE = "mongodb+srv://<db_username>:<db_password>@algoforgecluster.k77kly1.mongodb.net/?retryWrites=true&w=majority&appName=algoforgecluster"
DEFAULT_DB_NAME = "algoforge"

class MongoUser:
    """Wrapper class providing both attribute and dictionary access for compatibility."""
    def __init__(self, doc: Dict[str, Any]):
        self._doc = dict(doc or {})
        self.email = self._doc.get("email", "")
        self.username = self._doc.get("username", "")
        self.password = self._doc.get("password", "")
        self.avatar = self._doc.get("avatar")
        self.theme = self._doc.get("theme", "orange")
        self.score = self._doc.get("score", 0)
        self.latency = self._doc.get("latency", 0.0)
        self.tests = self._doc.get("tests", "0/36 Verified")
        self.status = self._doc.get("status", "enrolled")
        self.registered_at = self._doc.get("registered_at", int(time.time() * 1000))
        
        # Problems solved list
        p_solved = self._doc.get("problems_solved", [])
        if isinstance(p_solved, str):
            try: p_solved = json.loads(p_solved)
            except Exception: p_solved = []
        self._problems_solved_list = p_solved
        self.problems_solved = json.dumps(p_solved)
        self.solved_count = len(p_solved)
        
        self.attempts_count = self._doc.get("attempts_count", 0)
        
        # Recent submissions
        r_subs = self._doc.get("recent_submissions", [])
        if isinstance(r_subs, str):
            try: r_subs = json.loads(r_subs)
            except Exception: r_subs = []
        self._recent_subs_list = r_subs
        self.recent_submissions = json.dumps(r_subs)
        
        # Learning progress
        l_prog = self._doc.get("learning_progress", [])
        if isinstance(l_prog, str):
            try: l_prog = json.loads(l_prog)
            except Exception: l_prog = []
        self._learning_progress_list = l_prog
        self.learning_progress = json.dumps(l_prog)
        
        # Saved code
        s_code = self._doc.get("saved_code", {})
        if isinstance(s_code, str):
            try: s_code = json.loads(s_code)
            except Exception: s_code = {}
        self._saved_code_dict = s_code
        self.saved_code = json.dumps(s_code)
        
        self.updated_at = self._doc.get("updated_at", int(time.time() * 1000))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "email": self.email,
            "username": self.username,
            "avatar": self.avatar or f"https://api.dicebear.com/7.x/identicon/svg?seed={self.username or 'cadet'}",
            "theme": self.theme or "orange",
            "score": self.score or 0,
            "latency": self.latency or 0.0,
            "tests": self.tests or f"{self.solved_count}/36 Verified",
            "status": self.status or ("solving" if self.score > 0 else "enrolled"),
            "registeredAt": self.registered_at,
            "problemsSolved": self._problems_solved_list,
            "solvedCount": self.solved_count,
            "attemptsCount": self.attempts_count,
            "recentSubmissions": self._recent_subs_list,
            "learningProgress": self._learning_progress_list,
            "savedCode": self._saved_code_dict,
            "updatedAt": self.updated_at
        }


class MongoDBManager:
    """Manages connection, seeding, and CRUD operations on MongoDB Atlas."""
    def __init__(self):
        self.client: Optional[MongoClient] = None
        self.db = None
        self.users_coll = None
        self.reg_logs_coll = None
        self.sub_logs_coll = None
        self.is_connected = False
        self.connection_error: Optional[str] = None
        self.has_placeholders = False
        self.active_uri_masked = ""

    def resolve_connection_uri(self) -> str:
        uri = os.getenv("MONGODB_URI", DEFAULT_MONGO_URI_TEMPLATE).strip()
        user = os.getenv("MONGODB_USER") or os.getenv("MONGO_USER")
        pwd = os.getenv("MONGODB_PASSWORD") or os.getenv("MONGODB_PASS") or os.getenv("MONGO_PASSWORD")

        if user and pwd:
            escaped_user = urllib.parse.quote_plus(user)
            escaped_pwd = urllib.parse.quote_plus(pwd)
            if "<db_username>" in uri:
                uri = uri.replace("<db_username>", escaped_user)
            if "<db_password>" in uri:
                uri = uri.replace("<db_password>", escaped_pwd)

        return uri

    def init_connection(self) -> bool:
        if not PYMONGO_AVAILABLE:
            self.connection_error = "PyMongo is not installed in the current environment."
            print(f"[AlgoForge MongoDB] {self.connection_error}")
            return False

        uri = self.resolve_connection_uri()
        db_name = os.getenv("MONGODB_DATABASE", DEFAULT_DB_NAME).strip()

        # Check for placeholders
        if "<db_username>" in uri or "<db_password>" in uri:
            self.has_placeholders = True
            self.is_connected = False
            self.connection_error = "Connection string contains placeholder credentials (<db_username>:<db_password>)."
            print("[AlgoForge MongoDB] Notice: MongoDB Atlas URI configured with placeholders (<db_username>:<db_password>).")
            print("[AlgoForge MongoDB] To activate MongoDB Atlas, update MONGODB_URI or MONGODB_USER/MONGODB_PASSWORD in .env.")
            return False

        # Mask password for display
        try:
            if "@" in uri:
                prefix, host_part = uri.split("@", 1)
                proto = prefix.split("://")[0]
                self.active_uri_masked = f"{proto}://*****:*****@{host_part.split('?')[0]}"
            else:
                self.active_uri_masked = "mongodb://*****"
        except Exception:
            self.active_uri_masked = "mongodb+srv://algoforgecluster"

        try:
            print(f"[AlgoForge MongoDB] Attempting connection to MongoDB Atlas ({self.active_uri_masked})...")
            self.client = MongoClient(
                uri,
                serverSelectionTimeoutMS=3000,
                connectTimeoutMS=3000,
                socketTimeoutMS=5000,
                retryWrites=True
            )
            # Ping database to confirm authentication and connectivity
            self.client.admin.command('ping')
            self.db = self.client[db_name]
            self.users_coll = self.db["users"]
            self.reg_logs_coll = self.db["registration_logs"]
            self.sub_logs_coll = self.db["submission_logs"]

            # Create unique index on email
            self.users_coll.create_index("email", unique=True)
            self.reg_logs_coll.create_index("email")
            self.sub_logs_coll.create_index("user_email")

            self.is_connected = True
            self.connection_error = None
            print(f"[AlgoForge MongoDB] SUCCESS: Connected to MongoDB Atlas database '{db_name}'.")

            # Seed existing verified accounts if users collection is empty
            self.seed_users_if_empty()
            return True

        except (ServerSelectionTimeoutError, ConnectionFailure) as e:
            self.is_connected = False
            self.connection_error = f"Network or timeout error connecting to MongoDB Atlas: {e}"
            print(f"[AlgoForge MongoDB] WARNING: {self.connection_error}")
            return False
        except ConfigurationError as e:
            self.is_connected = False
            self.connection_error = f"Configuration/Authentication error: {e}"
            print(f"[AlgoForge MongoDB] WARNING: {self.connection_error}")
            return False
        except Exception as e:
            self.is_connected = False
            self.connection_error = str(e)
            print(f"[AlgoForge MongoDB] WARNING: Unexpected connection error: {e}")
            return False

    def seed_users_if_empty(self):
        """Auto-seeds verified accounts from registered_users.json into MongoDB."""
        if not self.is_connected or self.users_coll is None:
            return
        try:
            count = self.users_coll.count_documents({})
            if count == 0:
                users_file = os.path.join(os.path.dirname(__file__), "registered_users.json")
                if os.path.exists(users_file):
                    with open(users_file, "r", encoding="utf-8") as f:
                        reg_data = json.load(f)
                    now_ts = int(time.time() * 1000)
                    seeded_count = 0
                    for email_key, u_info in reg_data.items():
                        email_clean = email_key.strip().lower()
                        doc = {
                            "_id": email_clean,
                            "email": email_clean,
                            "username": u_info.get("username", email_clean.split("@")[0]),
                            "password": u_info.get("password", "DefaultPass123!"),
                            "avatar": u_info.get("avatar") or f"https://api.dicebear.com/7.x/identicon/svg?seed={email_clean.split('@')[0]}",
                            "theme": u_info.get("theme", "orange"),
                            "score": u_info.get("score", 0),
                            "latency": u_info.get("latency", 0.0),
                            "tests": u_info.get("tests", "0/36 Verified"),
                            "status": u_info.get("status", "enrolled"),
                            "registered_at": u_info.get("registeredAt", now_ts),
                            "problems_solved": u_info.get("problemsSolved", []),
                            "solved_count": len(u_info.get("problemsSolved", [])),
                            "attempts_count": u_info.get("attemptsCount", 0),
                            "recent_submissions": u_info.get("recentSubmissions", []),
                            "learning_progress": u_info.get("learningProgress", []),
                            "saved_code": u_info.get("savedCode", {}),
                            "updated_at": now_ts
                        }
                        self.users_coll.replace_one({"email": email_clean}, doc, upsert=True)
                        seeded_count += 1
                    print(f"[AlgoForge MongoDB] Seeded {seeded_count} verified users into MongoDB Atlas collection 'users'.")
        except Exception as e:
            print(f"[AlgoForge MongoDB] Notice during user seeding: {e}")

    # =========================================================================
    # USER OPERATIONS
    # =========================================================================
    def get_user(self, email: str) -> Optional[MongoUser]:
        if not self.is_connected or self.users_coll is None:
            return None
        try:
            norm_email = email.strip().lower()
            doc = self.users_coll.find_one({"email": norm_email})
            return MongoUser(doc) if doc else None
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error reading user {email}: {e}")
            return None

    def create_user(self, email: str, username: str, password: str, avatar: Optional[str] = None, theme: str = "orange") -> Optional[MongoUser]:
        if not self.is_connected or self.users_coll is None:
            return None
        try:
            norm_email = email.strip().lower()
            now_ts = int(time.time() * 1000)
            existing = self.users_coll.find_one({"email": norm_email})
            if existing:
                update_fields = {"updated_at": now_ts}
                if username: update_fields["username"] = username
                if password: update_fields["password"] = password
                if avatar: update_fields["avatar"] = avatar
                if theme: update_fields["theme"] = theme
                self.users_coll.update_one({"email": norm_email}, {"$set": update_fields})
                return MongoUser(self.users_coll.find_one({"email": norm_email}))
            else:
                doc = {
                    "_id": norm_email,
                    "email": norm_email,
                    "username": username,
                    "password": password,
                    "avatar": avatar or f"https://api.dicebear.com/7.x/identicon/svg?seed={username}",
                    "theme": theme or "orange",
                    "score": 0,
                    "latency": 0.0,
                    "tests": "0/36 Verified",
                    "status": "enrolled",
                    "registered_at": now_ts,
                    "problems_solved": [],
                    "solved_count": 0,
                    "attempts_count": 0,
                    "recent_submissions": [],
                    "learning_progress": [],
                    "saved_code": {},
                    "updated_at": now_ts
                }
                self.users_coll.insert_one(doc)
                return MongoUser(doc)
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error creating user {email}: {e}")
            return None

    def update_profile(self, email: str, avatar: Optional[str] = None, theme: Optional[str] = None, score: Optional[int] = None, latency: Optional[float] = None, tests: Optional[str] = None) -> Optional[MongoUser]:
        if not self.is_connected or self.users_coll is None:
            return None
        try:
            norm_email = email.strip().lower()
            existing = self.users_coll.find_one({"email": norm_email})
            if not existing:
                return None
            update_fields = {"updated_at": int(time.time() * 1000)}
            if avatar: update_fields["avatar"] = avatar
            if theme: update_fields["theme"] = theme
            if score is not None: update_fields["score"] = max(existing.get("score", 0), score)
            if latency is not None: update_fields["latency"] = latency
            if tests is not None: update_fields["tests"] = tests
            self.users_coll.update_one({"email": norm_email}, {"$set": update_fields})
            return MongoUser(self.users_coll.find_one({"email": norm_email}))
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error updating profile {email}: {e}")
            return None

    def record_user_submission(
        self,
        email: str,
        problem_id: str,
        mode: str = "challenge",
        score_delta: int = 10,
        latency: float = 0.8,
        passed: bool = True,
        code: str = "",
        language: str = "python",
        submission_details: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        if not self.is_connected or self.users_coll is None:
            return None
        try:
            norm_email = email.strip().lower()
            user = self.users_coll.find_one({"email": norm_email})
            if not user:
                return None

            solved_list = list(user.get("problems_solved") or [])
            is_new_solve = False
            new_score = user.get("score", 0)
            if passed and problem_id:
                if problem_id not in solved_list:
                    solved_list.append(problem_id)
                    new_score = new_score + score_delta
                    is_new_solve = True

            attempts_count = user.get("attempts_count", 0) + 1
            current_lat = user.get("latency", 0.0)
            new_lat = round((current_lat + latency) / 2.0, 2) if (current_lat > 0 and latency > 0) else (round(latency, 2) if latency > 0 else current_lat)

            now_ts = int(time.time() * 1000)
            sub_title = (submission_details.get("title") if submission_details else None) or problem_id
            sub_code = code or (submission_details.get("code") if submission_details else "") or ""
            sub_lang = language or (submission_details.get("language") if submission_details else "python") or "python"

            sub_rec = {
                "id": f"SUB-{now_ts}",
                "problemId": problem_id,
                "problemTitle": sub_title,
                "mode": mode,
                "status": "PASS" if passed else "FAIL",
                "passed": passed,
                "score": score_delta if passed else 0,
                "latency": latency,
                "runtime": f"{latency} ms",
                "memory": f"{round(12.0 + (latency * 2.5), 1)} MB",
                "timestamp": now_ts,
                "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
                "language": sub_lang,
                "code": sub_code,
                "failureReason": None if passed else "Test assertions incomplete"
            }

            subs_list = [sub_rec] + list(user.get("recent_submissions") or [])
            subs_list = subs_list[:30]

            update_fields = {
                "problems_solved": solved_list,
                "solved_count": len(solved_list),
                "score": new_score,
                "attempts_count": attempts_count,
                "latency": new_lat,
                "tests": f"{len(solved_list)}/36 Verified",
                "status": "solving" if (passed or user.get("status") == "solving") else user.get("status", "enrolled"),
                "recent_submissions": subs_list,
                "updated_at": now_ts
            }
            self.users_coll.update_one({"email": norm_email}, {"$set": update_fields})

            # Record in submission logs
            if self.sub_logs_coll is not None:
                self.sub_logs_coll.insert_one({
                    "user_email": norm_email,
                    "problem_id": problem_id,
                    "mode": mode,
                    "score": score_delta if passed else 0,
                    "latency": latency,
                    "passed": passed,
                    "created_at": datetime.utcnow()
                })

            updated_doc = self.users_coll.find_one({"email": norm_email})
            return MongoUser(updated_doc).to_dict()
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error recording user submission {email}: {e}")
            return None

    def save_user_code(self, email: str, problem_id: str, code: str) -> bool:
        if not self.is_connected or self.users_coll is None:
            return False
        try:
            norm_email = email.strip().lower()
            user = self.users_coll.find_one({"email": norm_email})
            if not user:
                return False
            code_map = dict(user.get("saved_code") or {})
            code_map[problem_id] = code
            self.users_coll.update_one(
                {"email": norm_email},
                {"$set": {"saved_code": code_map, "updated_at": int(time.time() * 1000)}}
            )
            return True
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error saving code {email}: {e}")
            return False

    def update_learning_progress(self, email: str, algo_id: str, problem_id: Optional[str] = None) -> bool:
        if not self.is_connected or self.users_coll is None:
            return False
        try:
            norm_email = email.strip().lower()
            user = self.users_coll.find_one({"email": norm_email})
            if not user:
                return False
            progress_list = list(user.get("learning_progress") or [])
            entry = {"algoId": algo_id, "problemId": problem_id, "completedAt": int(time.time() * 1000)}
            if not any(p.get("algoId") == algo_id and p.get("problemId") == problem_id for p in progress_list):
                progress_list.append(entry)
                self.users_coll.update_one(
                    {"email": norm_email},
                    {"$set": {"learning_progress": progress_list, "updated_at": int(time.time() * 1000)}}
                )
            return True
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error updating learning progress {email}: {e}")
            return False

    def get_all_users(self) -> List[Dict[str, Any]]:
        if not self.is_connected or self.users_coll is None:
            return []
        try:
            cursor = self.users_coll.find({}).sort([("score", -1), ("latency", 1)])
            return [MongoUser(doc).to_dict() for doc in cursor]
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error getting all users: {e}")
            return []

    # =========================================================================
    # AUDIT LOGS
    # =========================================================================
    def log_registration(self, email: str, username: Optional[str] = None, status: str = "SUCCESS", ip_address: Optional[str] = None):
        if not self.is_connected or self.reg_logs_coll is None:
            return
        try:
            self.reg_logs_coll.insert_one({
                "email": email.strip().lower(),
                "username": username,
                "status": status,
                "ip_address": ip_address,
                "created_at": datetime.utcnow()
            })
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error logging registration: {e}")

    def get_registration_logs(self, limit: int = 50) -> List[Dict[str, Any]]:
        if not self.is_connected or self.reg_logs_coll is None:
            return []
        try:
            cursor = self.reg_logs_coll.find({}).sort("created_at", -1).limit(limit)
            out = []
            for doc in cursor:
                out.append({
                    "id": str(doc.get("_id")),
                    "email": doc.get("email"),
                    "username": doc.get("username"),
                    "status": doc.get("status"),
                    "ipAddress": doc.get("ip_address"),
                    "createdAt": doc.get("created_at").isoformat() if doc.get("created_at") else None
                })
            return out
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error getting registration logs: {e}")
            return []

    def log_submission(self, email: str, problem_id: Optional[str] = None, mode: str = "challenge", score: int = 0, latency: float = 0.0, passed: bool = False):
        if not self.is_connected or self.sub_logs_coll is None:
            return
        try:
            self.sub_logs_coll.insert_one({
                "user_email": email.strip().lower(),
                "problem_id": problem_id,
                "mode": mode,
                "score": score,
                "latency": latency,
                "passed": passed,
                "created_at": datetime.utcnow()
            })
        except Exception as e:
            print(f"[AlgoForge MongoDB] Error logging submission: {e}")


# Global MongoDB Manager Singleton
mongo_manager = MongoDBManager()
