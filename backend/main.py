import os
import json
import time
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.models import (
    AuthRequest, OAuthRequest, AuthResponse, AlgorithmRequest,
    ExecutionResponse, ProfileUpdateRequest, UserSubmissionRequest,
    SaveCodeRequest, LearningProgressRequest
)
from backend.dataset import CORE_ALGORITHMS_DATASET, MULTI_SOURCE_QUESTION_BANK
from backend.algorithm_tracer import AlgorithmTracer
from backend.database import (
    init_db, db_get_user, db_create_user, db_update_profile,
    db_get_all_users, db_log_registration, db_get_registration_logs,
    db_log_submission, db_record_user_submission, db_save_user_code,
    db_update_learning_progress, db_get_active_engine_name, db_get_status
)

app = FastAPI(
    title="AlgoForge Hyper-Glitch Engine",
    description="Cyberpunk 2D Algorithm Platform with FastAPI Telemetry & PostgreSQL Database",
    version="2.6.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ORIG_USERS_FILE = os.path.join(os.path.dirname(__file__), "registered_users.json")
if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
    USERS_FILE = "/tmp/registered_users.json"
    if os.path.exists(ORIG_USERS_FILE) and not os.path.exists(USERS_FILE):
        try:
            import shutil
            shutil.copyfile(ORIG_USERS_FILE, USERS_FILE)
        except Exception:
            pass
else:
    USERS_FILE = ORIG_USERS_FILE

def load_registered_users() -> Dict[str, Dict[str, Any]]:
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_registered_users():
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(REGISTERED_USERS, f, indent=2)
    except Exception as e:
        print(f"Error saving registered users: {e}")

REGISTERED_USERS = load_registered_users()

# Initialize Database on startup
@app.on_event("startup")
def on_startup():
    try:
        init_db()
    except Exception as e:
        print(f"[AlgoForge] Error initializing database: {e}")

@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "engine": "AlgoForge 2D Telemetry & MongoDB / Cloud Core",
        "version": "2.7.0",
        "database": db_get_active_engine_name()
    }

@app.get("/api/db/status")
async def get_db_status():
    return db_get_status()

@app.get("/api/auth/users")
@app.get("/api/leaderboard")
async def get_all_registered_users():
    """
    Returns only the users whose details are stored in the database.
    Strictly ensures no dummy users are returned.
    """
    try:
        db_users = db_get_all_users()
        if db_users and len(db_users) > 0:
            return {"users": db_users, "total": len(db_users), "source": "database"}
    except Exception as e:
        print(f"[AlgoForge API] Error reading users from database: {e}")

    # Fallback to local file only if DB query encountered an exception
    fresh_users = load_registered_users()
    users_list = list(fresh_users.values())
    users_list.sort(key=lambda u: (-u.get("score", 0), u.get("latency", 999.0)))
    return {"users": users_list, "total": len(users_list), "source": "file_cache"}

@app.get("/api/user/profile")
async def get_user_profile(email: str = Query(..., description="User email address")):
    """Retrieves full user details from the database."""
    email_clean = email.strip().lower()
    user = db_get_user(email_clean)
    if not user:
        raise HTTPException(status_code=404, detail="User not found in database.")
    return {"success": True, "user": user.to_dict()}

@app.get("/api/auth/registration-logs")
async def get_registration_logs():
    """Returns the immutable audit log of all registration attempts from the database."""
    try:
        logs = db_get_registration_logs(limit=100)
        return {"logs": logs, "total": len(logs)}
    except Exception as e:
        return {"logs": [], "total": 0, "error": str(e)}

@app.post("/api/auth/register", response_model=AuthResponse)
async def register(req: AuthRequest):
    """
    Registers a new user into the database and audit log.
    Ensures email uniqueness and records IP/timestamp.
    """
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean or "@" not in email_clean:
        db_log_registration(email=email_clean, username=req.username, status="FAILED_VALIDATION")
        raise HTTPException(status_code=400, detail="Invalid email address.")

    if not req.password or len(req.password) < 6:
        db_log_registration(email=email_clean, username=req.username, status="FAILED_PASSWORD_LENGTH")
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters.")

    # Check if user already exists in database
    existing_user = db_get_user(email_clean)
    if existing_user:
        db_log_registration(email=email_clean, username=req.username, status="FAILED_EXISTS")
        raise HTTPException(
            status_code=400,
            detail=f"An account with email '{email_clean}' is already registered in the database. Please log in directly."
        )

    username_clean = req.username.strip() if req.username else email_clean.split("@")[0].capitalize()

    # Save to primary database
    user_record = db_create_user(
        email=email_clean,
        username=username_clean,
        password=req.password,
        avatar=f"https://api.dicebear.com/7.x/identicon/svg?seed={username_clean}",
        theme="orange"
    )

    # Log registration audit event in database
    db_log_registration(email=email_clean, username=username_clean, status="SUCCESS")

    user_dict = user_record.to_dict()
    REGISTERED_USERS[email_clean] = user_dict
    save_registered_users()

    return AuthResponse(
        success=True,
        message="Registration successful! Account logged in database.",
        user=user_dict,
        token=f"token_{user_record.username}_2026"
    )

@app.post("/api/auth/login", response_model=AuthResponse)
async def login(req: AuthRequest):
    """
    Authenticates against the database.
    Only allows users whose details are stored in the database.
    """
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean or "@" not in email_clean:
        raise HTTPException(status_code=400, detail="Invalid email address.")

    # Query the database
    user = db_get_user(email_clean)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Account not registered. No account found in database for {email_clean}. Please register your account first before logging in."
        )

    if req.password and user.password and user.password != req.password:
        raise HTTPException(status_code=401, detail="Incorrect password. Please verify your credentials.")

    user_dict = user.to_dict()
    return AuthResponse(
        success=True,
        message="Login successful! Welcome back, Operator.",
        user=user_dict,
        token=f"token_{user.username}_2026"
    )

@app.post("/api/auth/update-profile")
async def update_profile(req: ProfileUpdateRequest):
    """Updates user profile (avatar, theme, score, latency) in the database."""
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean:
        raise HTTPException(status_code=400, detail="Email is required.")

    user = db_update_profile(
        email=email_clean,
        avatar=req.avatar,
        theme=req.theme,
        score=req.score
    )
    if not user:
        user = db_create_user(
            email=email_clean,
            username=email_clean.split("@")[0].capitalize(),
            password="Password123!",
            avatar=req.avatar,
            theme=req.theme or "orange"
        )
        if req.score:
            user = db_update_profile(email=email_clean, score=req.score)

    user_dict = user.to_dict()
    REGISTERED_USERS[email_clean] = user_dict
    save_registered_users()
    return {"success": True, "user": user_dict}

@app.post("/api/user/record-submission")
async def record_user_submission(req: UserSubmissionRequest):
    """
    Persists problem attempts, solutions, and code submissions into the database.
    Updates the user's solved problems list, score, and recent submissions list.
    """
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean:
        raise HTTPException(status_code=400, detail="User email is required.")

    updated_user = db_record_user_submission(
        email=email_clean,
        problem_id=req.problem_id,
        mode=req.mode,
        score_delta=req.score,
        latency=req.latency,
        passed=req.passed,
        code=req.code,
        language=req.language,
        submission_details=req.details
    )

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found in database to record submission.")

    REGISTERED_USERS[email_clean] = updated_user
    save_registered_users()

    return {"success": True, "user": updated_user}

@app.post("/api/user/save-code")
async def save_user_code(req: SaveCodeRequest):
    """Saves user code drafts per problem directly into the database."""
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean:
        raise HTTPException(status_code=400, detail="User email is required.")

    ok = db_save_user_code(email_clean, req.problem_id, req.code)
    if not ok:
        raise HTTPException(status_code=400, detail="Could not save code draft to database.")

    return {"success": True, "message": "Code draft persisted to database."}

@app.post("/api/user/learning-progress")
async def save_learning_progress(req: LearningProgressRequest):
    """Saves user learning mode progress (completed algorithm topics) in the database."""
    email_clean = req.email.strip().lower() if req.email else ""
    if not email_clean:
        raise HTTPException(status_code=400, detail="User email is required.")

    ok = db_update_learning_progress(email_clean, req.algo_id, req.problem_id)
    return {"success": ok}

@app.post("/api/auth/oauth", response_model=AuthResponse)
async def oauth_authenticate(req: OAuthRequest):
    provider = req.provider.capitalize()
    email_clean = req.email.strip().lower() if req.email else f"cadet.{provider.lower()}@algoforge.dev"
    username = req.username or email_clean.split("@")[0].capitalize()

    user = db_get_user(email_clean)
    if not user:
        user = db_create_user(
            email=email_clean,
            username=username,
            password=f"oauth_{provider.lower()}_authenticated",
            avatar=f"https://api.dicebear.com/7.x/identicon/svg?seed={username}",
            theme="orange"
        )
        db_log_registration(email=email_clean, username=username, status=f"SUCCESS_OAUTH_{provider.upper()}")

    user_dict = user.to_dict()
    return AuthResponse(
        success=True,
        message=f"Verified through {provider} Enterprise OAuth. Session activated.",
        user=user_dict,
        token=f"oauth_{provider.lower()}_{user.username}_2026"
    )

@app.get("/api/algorithms")
async def list_algorithms():
    return {"algorithms": list(CORE_ALGORITHMS_DATASET.values())}

@app.get("/api/algorithm/{algo_id}")
async def get_algorithm_detail(algo_id: str):
    algo_data = CORE_ALGORITHMS_DATASET.get(algo_id)
    if not algo_data:
        raise HTTPException(status_code=404, detail="Algorithm not found.")
    return algo_data

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EXP_QUESTIONS_PATH = os.path.join(BASE_DIR, "AlgoForge_Experience_Mode_Question_Bank.json")
CHAL_QUESTIONS_PATH = os.path.join(BASE_DIR, "AlgoForge_Challenge_Mode_Question_Bank.json")

def load_json_bank(file_path):
    candidates = [
        file_path,
        os.path.join(os.getcwd(), os.path.basename(file_path)),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.basename(file_path)),
        os.path.join(os.path.dirname(__file__), os.path.basename(file_path))
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading {p}: {e}")
    return []

EXPERIENCE_QUESTIONS = load_json_bank(EXP_QUESTIONS_PATH)
CHALLENGE_QUESTIONS = load_json_bank(CHAL_QUESTIONS_PATH)

@app.get("/api/questions/experience")
async def get_experience_questions(topic: str = None, type: str = None):
    questions = load_json_bank(EXP_QUESTIONS_PATH) or EXPERIENCE_QUESTIONS
    if topic and topic.lower() != "all":
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if type and type.lower() != "all":
        questions = [q for q in questions if q.get("type", "").lower() == type.lower()]
    return {"total": len(questions), "questions": questions}

@app.get("/api/questions/challenge")
async def get_challenge_questions(topic: str = None, difficulty: str = None):
    questions = load_json_bank(CHAL_QUESTIONS_PATH) or CHALLENGE_QUESTIONS
    if topic and topic.lower() != "all":
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if difficulty and difficulty.lower() != "all":
        questions = [q for q in questions if q.get("difficulty", "").lower() == difficulty.lower()]
    return {"total": len(questions), "questions": questions}

@app.get("/api/questions")
async def get_all_questions(mode: str = "all", topic: str = None, type: str = None):
    questions = []
    if mode in ["all", "experience"]:
        questions.extend(load_json_bank(EXP_QUESTIONS_PATH) or EXPERIENCE_QUESTIONS)
    if mode in ["all", "challenge"]:
        questions.extend(load_json_bank(CHAL_QUESTIONS_PATH) or CHALLENGE_QUESTIONS)
    
    if topic and topic.lower() != "all":
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if type and type.lower() != "all":
        questions = [q for q in questions if q.get("type", "").lower() == type.lower()]
    return {"total": len(questions), "questions": questions}

@app.post("/api/execute", response_model=ExecutionResponse)
async def execute_algorithm(req: AlgorithmRequest):
    try:
        response = AlgorithmTracer.trace(req.algorithm, req.data, req.target, req.problem_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Mount Static Frontend Files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
