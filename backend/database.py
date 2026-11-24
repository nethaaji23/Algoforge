import os
import time
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine, Column, String, Integer, Float, BigInteger, Text, Boolean, DateTime, inspect, text
)
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from backend.mongo_db import mongo_manager, MongoUser

# Load environment variables
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

DEFAULT_NEON_URL = (
    "postgresql://neondb_owner:npg_2saDWoIA3tiP@ep-proud-bar-b4voafnv-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require"
)

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_NEON_URL)

# SQLAlchemy expects postgresql:// (not postgres://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

Base = declarative_base()

class DBUser(Base):
    __tablename__ = "users"

    email = Column(String(255), primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    avatar = Column(Text, nullable=True)
    theme = Column(String(50), default="orange")
    score = Column(Integer, default=0)
    latency = Column(Float, default=0.0)
    tests = Column(String(50), default="0/36 Verified")
    status = Column(String(50), default="enrolled")
    registered_at = Column(BigInteger, default=lambda: int(time.time() * 1000))

    # Comprehensive user progress and submission storage
    problems_solved = Column(Text, default="[]")
    solved_count = Column(Integer, default=0)
    attempts_count = Column(Integer, default=0)
    recent_submissions = Column(Text, default="[]")
    learning_progress = Column(Text, default="[]")
    saved_code = Column(Text, default="{}")
    updated_at = Column(BigInteger, default=lambda: int(time.time() * 1000))

    def to_dict(self) -> Dict[str, Any]:
        try:
            solved_list = json.loads(self.problems_solved) if self.problems_solved else []
        except Exception:
            solved_list = []

        try:
            subs_list = json.loads(self.recent_submissions) if self.recent_submissions else []
        except Exception:
            subs_list = []

        try:
            learning_list = json.loads(self.learning_progress) if self.learning_progress else []
        except Exception:
            learning_list = []

        try:
            code_map = json.loads(self.saved_code) if self.saved_code else {}
        except Exception:
            code_map = {}

        return {
            "email": self.email,
            "username": self.username,
            "avatar": self.avatar or f"https://api.dicebear.com/7.x/identicon/svg?seed={self.username}",
            "theme": self.theme or "orange",
            "score": self.score or 0,
            "latency": self.latency or 0.0,
            "tests": self.tests or f"{self.solved_count or len(solved_list)}/36 Verified",
            "status": self.status or ("solving" if (self.score and self.score > 0) else "enrolled"),
            "registeredAt": self.registered_at or int(time.time() * 1000),
            "problemsSolved": solved_list,
            "solvedCount": self.solved_count or len(solved_list),
            "attemptsCount": self.attempts_count or 0,
            "recentSubmissions": subs_list,
            "learningProgress": learning_list,
            "savedCode": code_map,
            "updatedAt": self.updated_at or int(time.time() * 1000)
        }

class DBRegistrationLog(Base):
    __tablename__ = "registration_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, index=True)
    username = Column(String(100), nullable=True)
    status = Column(String(50), nullable=False)  # SUCCESS, FAILED_EXISTS, FAILED_VALIDATION
    ip_address = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "status": self.status,
            "ipAddress": self.ip_address,
            "createdAt": self.created_at.isoformat() if self.created_at else None
        }

class DBSubmissionLog(Base):
    __tablename__ = "submission_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(255), nullable=False, index=True)
    problem_id = Column(String(100), nullable=True)
    mode = Column(String(50), default="challenge")
    score = Column(Integer, default=0)
    latency = Column(Float, default=0.0)
    passed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "userEmail": self.user_email,
            "problemId": self.problem_id,
            "mode": self.mode,
            "score": self.score,
            "latency": self.latency,
            "passed": self.passed,
            "createdAt": self.created_at.isoformat() if self.created_at else None
        }

def create_db_engine():
    """Create database engine with automatic fallback to local SQLite if remote PostgreSQL is unreachable."""
    try:
        if "postgresql" in DATABASE_URL and "@" in DATABASE_URL:
            import socket
            import concurrent.futures
            host = DATABASE_URL.split("@")[1].split("/")[0].split(":")[0]
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            try:
                future = executor.submit(socket.gethostbyname, host)
                ip = future.result(timeout=0.8)
                if not ip:
                    raise ConnectionError("DNS resolution failed for PostgreSQL host.")
            finally:
                try:
                    executor.shutdown(wait=False, cancel_futures=True)
                except TypeError:
                    executor.shutdown(wait=False)

        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            connect_args={"connect_timeout": 2} if "postgresql" in DATABASE_URL else {}
        )
        with engine.connect() as conn:
            pass
        print(f"[AlgoForge Database] Connected successfully to primary database: {DATABASE_URL.split('@')[-1] if '@' in DATABASE_URL else DATABASE_URL}")
        return engine
    except Exception as e:
        print(f"[AlgoForge Database] WARNING: Could not connect to primary database ({e}). Falling back to local SQLite.")
        if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
            sqlite_path = "/tmp/algoforge.db"
            # Copy existing local db to /tmp if it doesn't exist yet
            orig_path = os.path.join(os.path.dirname(__file__), "algoforge.db")
            if os.path.exists(orig_path) and not os.path.exists(sqlite_path):
                try:
                    import shutil
                    shutil.copyfile(orig_path, sqlite_path)
                except Exception:
                    pass
        else:
            sqlite_path = os.path.join(os.path.dirname(__file__), "algoforge.db")
        fallback_url = f"sqlite:///{sqlite_path}"
        engine = create_engine(fallback_url, connect_args={"check_same_thread": False})
        return engine

engine = create_db_engine()
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    """Initializes MongoDB Atlas connection or falls back to relational database."""
    # 1. Attempt MongoDB Atlas Connection
    try:
        mongo_manager.init_connection()
        if mongo_manager.is_connected:
            print("[AlgoForge Database] Connected to MongoDB Atlas! Using MongoDB as primary storage.")
        else:
            print("[AlgoForge Database] MongoDB Atlas inactive/pending credentials. Using relational fallback.")
    except Exception as e:
        print(f"[AlgoForge Database] Notice during MongoDB connection check: {e}")

    # 2. Relational Storage Initialization & Fallback Readiness
    Base.metadata.create_all(bind=engine)
    
    # Auto-migrate any missing columns for PostgreSQL or SQLite
    try:
        with engine.connect() as conn:
            is_pg = "postgresql" in str(engine.url)
            if is_pg:
                stmts = [
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS problems_solved TEXT DEFAULT '[]';",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS solved_count INTEGER DEFAULT 0;",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS attempts_count INTEGER DEFAULT 0;",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS recent_submissions TEXT DEFAULT '[]';",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS learning_progress TEXT DEFAULT '[]';",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS saved_code TEXT DEFAULT '{}';",
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS updated_at BIGINT;"
                ]
                for s in stmts:
                    try:
                        conn.execute(text(s))
                        conn.commit()
                    except Exception:
                        conn.rollback()
            else:
                # SQLite PRAGMA check
                info = conn.execute(text("PRAGMA table_info(users);")).fetchall()
                existing_cols = [r[1] for r in info]
                sqlite_cols = [
                    ("problems_solved", "TEXT DEFAULT '[]'"),
                    ("solved_count", "INTEGER DEFAULT 0"),
                    ("attempts_count", "INTEGER DEFAULT 0"),
                    ("recent_submissions", "TEXT DEFAULT '[]'"),
                    ("learning_progress", "TEXT DEFAULT '[]'"),
                    ("saved_code", "TEXT DEFAULT '{}'"),
                    ("updated_at", "BIGINT")
                ]
                for col_name, col_def in sqlite_cols:
                    if col_name not in existing_cols:
                        conn.execute(text(f"ALTER TABLE users ADD COLUMN {col_name} {col_def};"))
                conn.commit()
    except Exception as e:
        print(f"[AlgoForge Database] Notice during column auto-migration: {e}")

    print("[AlgoForge Database] Initialized and verified tables: users, registration_logs, submission_logs.")

    # Auto-seed verified users from registered_users.json if database is currently empty
    try:
        session = SessionLocal()
        if session.query(DBUser).count() == 0:
            users_file = os.path.join(os.path.dirname(__file__), "registered_users.json")
            if os.path.exists(users_file):
                with open(users_file, "r", encoding="utf-8") as f:
                    reg_data = json.load(f)
                for email_key, u_info in reg_data.items():
                    email_clean = email_key.strip().lower()
                    u_obj = DBUser(
                        email=email_clean,
                        username=u_info.get("username", email_clean.split("@")[0]),
                        password=u_info.get("password", "DefaultPass123!"),
                        avatar=u_info.get("avatar"),
                        theme=u_info.get("theme", "orange"),
                        score=u_info.get("score", 0),
                        latency=u_info.get("latency", 0.0),
                        tests=u_info.get("tests", "0/36 Verified"),
                        status=u_info.get("status", "enrolled"),
                        registered_at=u_info.get("registeredAt", int(time.time() * 1000)),
                        problems_solved=json.dumps(u_info.get("problemsSolved", [])),
                        solved_count=len(u_info.get("problemsSolved", [])),
                        attempts_count=u_info.get("attemptsCount", 0),
                        recent_submissions=json.dumps(u_info.get("recentSubmissions", [])),
                        learning_progress=json.dumps(u_info.get("learningProgress", [])),
                        saved_code=json.dumps(u_info.get("savedCode", {})),
                        updated_at=int(time.time() * 1000)
                    )
                    session.add(u_obj)
                session.commit()
                print(f"[AlgoForge Database] Seeded {len(reg_data)} verified users into database.")
        session.close()
    except Exception as e:
        print(f"[AlgoForge Database] Notice during user seeding: {e}")

# Database helper functions
def db_get_user(email: str):
    if mongo_manager.is_connected:
        return mongo_manager.get_user(email)
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        return session.query(DBUser).filter(DBUser.email == norm_email).first()
    finally:
        session.close()

def db_create_user(email: str, username: str, password: str, avatar: Optional[str] = None, theme: str = "orange"):
    if mongo_manager.is_connected:
        return mongo_manager.create_user(email, username, password, avatar, theme)
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        existing = session.query(DBUser).filter(DBUser.email == norm_email).first()
        now_ts = int(time.time() * 1000)
        if existing:
            if username:
                existing.username = username
            if password:
                existing.password = password
            if avatar:
                existing.avatar = avatar
            if theme:
                existing.theme = theme
            existing.updated_at = now_ts
            session.commit()
            session.refresh(existing)
            return existing
        else:
            new_user = DBUser(
                email=norm_email,
                username=username,
                password=password,
                avatar=avatar or f"https://api.dicebear.com/7.x/identicon/svg?seed={username}",
                theme=theme or "orange",
                score=0,
                latency=0.0,
                tests="0/36 Verified",
                status="enrolled",
                registered_at=now_ts,
                problems_solved="[]",
                solved_count=0,
                attempts_count=0,
                recent_submissions="[]",
                learning_progress="[]",
                saved_code="{}",
                updated_at=now_ts
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
    finally:
        session.close()

def db_update_profile(email: str, avatar: Optional[str] = None, theme: Optional[str] = None, score: Optional[int] = None, latency: Optional[float] = None, tests: Optional[str] = None):
    if mongo_manager.is_connected:
        return mongo_manager.update_profile(email, avatar, theme, score, latency, tests)
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        user = session.query(DBUser).filter(DBUser.email == norm_email).first()
        if not user:
            return None
        if avatar:
            user.avatar = avatar
        if theme:
            user.theme = theme
        if score is not None:
            user.score = max(user.score or 0, score)
            if user.score > 0:
                user.status = "solving"
        if latency is not None and latency > 0:
            user.latency = latency
        if tests:
            user.tests = tests
        user.updated_at = int(time.time() * 1000)
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()

def db_record_user_submission(
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
    """Records a real problem attempt/solve in the database, updating the user's solved list, score, and submissions."""
    if mongo_manager.is_connected:
        return mongo_manager.record_user_submission(
            email=email,
            problem_id=problem_id,
            mode=mode,
            score_delta=score_delta,
            latency=latency,
            passed=passed,
            code=code,
            language=language,
            submission_details=submission_details
        )
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        user = session.query(DBUser).filter(DBUser.email == norm_email).first()
        if not user:
            return None

        # Parse problems_solved
        try:
            solved_list = json.loads(user.problems_solved) if user.problems_solved else []
        except Exception:
            solved_list = []

        is_new_solve = False
        if passed and problem_id:
            if problem_id not in solved_list:
                solved_list.append(problem_id)
                user.problems_solved = json.dumps(solved_list)
                user.solved_count = len(solved_list)
                user.score = (user.score or 0) + score_delta
                is_new_solve = True
            user.status = "solving"

        # Update attempts count
        user.attempts_count = (user.attempts_count or 0) + 1

        # Update latency
        if latency and latency > 0:
            current_lat = user.latency or 0.0
            user.latency = round((current_lat + latency) / 2.0, 2) if current_lat > 0 else round(latency, 2)

        # Update tests badge
        user.tests = f"{len(solved_list)}/36 Verified"

        # Record submission object in recent_submissions
        try:
            subs_list = json.loads(user.recent_submissions) if user.recent_submissions else []
        except Exception:
            subs_list = []

        sub_rec = {
            "id": f"SUB-{int(time.time()*1000)}",
            "problemId": problem_id,
            "problemTitle": (submission_details.get("title") if submission_details else None) or problem_id,
            "mode": mode,
            "status": "PASS" if passed else "FAIL",
            "passed": passed,
            "score": score_delta if passed else 0,
            "latency": latency,
            "runtime": f"{latency:.2f} ms",
            "memory": "14.2 MB",
            "timestamp": int(time.time() * 1000),
            "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "language": language,
            "code": code,
            "failureReason": (submission_details.get("failureReason") if submission_details else None) if not passed else None
        }

        # Prepend to list and keep up to 50
        subs_list.insert(0, sub_rec)
        user.recent_submissions = json.dumps(subs_list[:50])

        # Also save user code draft
        if code and problem_id:
            try:
                code_map = json.loads(user.saved_code) if user.saved_code else {}
            except Exception:
                code_map = {}
            code_map[problem_id] = code
            user.saved_code = json.dumps(code_map)

        user.updated_at = int(time.time() * 1000)

        # Log into DBSubmissionLog
        log = DBSubmissionLog(
            user_email=norm_email,
            problem_id=problem_id,
            mode=mode,
            score=user.score,
            latency=latency,
            passed=passed
        )
        session.add(log)

        session.commit()
        session.refresh(user)
        return user.to_dict()
    except Exception as e:
        session.rollback()
        print(f"[AlgoForge Database] Failed to record user submission: {e}")
        return None
    finally:
        session.close()

def db_save_user_code(email: str, problem_id: str, code: str) -> bool:
    if mongo_manager.is_connected:
        return mongo_manager.save_user_code(email, problem_id, code)
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        user = session.query(DBUser).filter(DBUser.email == norm_email).first()
        if not user:
            return False
        try:
            code_map = json.loads(user.saved_code) if user.saved_code else {}
        except Exception:
            code_map = {}
        code_map[problem_id] = code
        user.saved_code = json.dumps(code_map)
        user.updated_at = int(time.time() * 1000)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"[AlgoForge Database] Error saving code: {e}")
        return False
    finally:
        session.close()

def db_update_learning_progress(email: str, algo_id: str, problem_id: Optional[str] = None) -> bool:
    if mongo_manager.is_connected:
        return mongo_manager.update_learning_progress(email, algo_id, problem_id)
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        user = session.query(DBUser).filter(DBUser.email == norm_email).first()
        if not user:
            return False
        try:
            prog = json.loads(user.learning_progress) if user.learning_progress else []
        except Exception:
            prog = []
        entry = {"algoId": algo_id, "problemId": problem_id, "completedAt": int(time.time() * 1000)}
        if not any(p.get("algoId") == algo_id and p.get("problemId") == problem_id for p in prog):
            prog.append(entry)
            user.learning_progress = json.dumps(prog)
            user.updated_at = int(time.time() * 1000)
            session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"[AlgoForge Database] Error saving learning progress: {e}")
        return False
    finally:
        session.close()

def db_get_all_users() -> List[Dict[str, Any]]:
    """Returns ONLY the registered users whose details are stored in the database, ordered by rank."""
    if mongo_manager.is_connected:
        return mongo_manager.get_all_users()
    session = SessionLocal()
    try:
        users = session.query(DBUser).order_by(DBUser.score.desc(), DBUser.latency.asc()).all()
        return [u.to_dict() for u in users]
    finally:
        session.close()

def db_log_registration(email: str, username: Optional[str] = None, status: str = "SUCCESS", ip_address: Optional[str] = None):
    if mongo_manager.is_connected:
        mongo_manager.log_registration(email, username, status, ip_address)
        return
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        log = DBRegistrationLog(
            email=norm_email,
            username=username,
            status=status,
            ip_address=ip_address
        )
        session.add(log)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"[AlgoForge Database] Failed to write registration log: {e}")
    finally:
        session.close()

def db_get_registration_logs(limit: int = 50) -> List[Dict[str, Any]]:
    if mongo_manager.is_connected:
        return mongo_manager.get_registration_logs(limit)
    session = SessionLocal()
    try:
        logs = session.query(DBRegistrationLog).order_by(DBRegistrationLog.id.desc()).limit(limit).all()
        return [l.to_dict() for l in logs]
    finally:
        session.close()

def db_log_submission(email: str, problem_id: Optional[str] = None, mode: str = "challenge", score: int = 0, latency: float = 0.0, passed: bool = False):
    if mongo_manager.is_connected:
        mongo_manager.log_submission(email, problem_id, mode, score, latency, passed)
        return
    session = SessionLocal()
    try:
        norm_email = email.strip().lower()
        log = DBSubmissionLog(
            user_email=norm_email,
            problem_id=problem_id,
            mode=mode,
            score=score,
            latency=latency,
            passed=passed
        )
        session.add(log)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"[AlgoForge Database] Failed to write submission log: {e}")
    finally:
        session.close()


def db_get_active_engine_name() -> str:
    if mongo_manager.is_connected:
        return "MongoDB Atlas Active (algoforgecluster)"
    elif "postgresql" in str(engine.url):
        return "NeonDB PostgreSQL Active"
    else:
        return "Local SQLite Active (Fallback)"

def db_get_status() -> Dict[str, Any]:
    return {
        "activeEngine": db_get_active_engine_name(),
        "mongoConnected": mongo_manager.is_connected,
        "mongoError": mongo_manager.connection_error,
        "mongoPlaceholders": mongo_manager.has_placeholders,
        "mongoUriMasked": mongo_manager.active_uri_masked,
        "sqlEngineUrl": str(engine.url).split("@")[-1] if "@" in str(engine.url) else str(engine.url)
    }
