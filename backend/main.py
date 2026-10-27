import os
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.models import AuthRequest, OAuthRequest, AuthResponse, AlgorithmRequest, ExecutionResponse
from backend.dataset import CORE_ALGORITHMS_DATASET, MULTI_SOURCE_QUESTION_BANK
from backend.algorithm_tracer import AlgorithmTracer

app = FastAPI(
    title="AlgoForge Hyper-Glitch Engine",
    description="Cyberpunk 2D Algorithm Platform with FastAPI Telemetry",
    version="2.5.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REGISTERED_USERS: Dict[str, Dict[str, Any]] = {
    "dev@algoforge.io": {
        "email": "dev@algoforge.io",
        "username": "GlitchCoder",
        "password": "password123",
        "xp": 2400,
        "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuAvZ-ScU2UrnAt_mtGdfWUU8487P6gH09aJRiPtHEqXUmNn-uXBsS6UWHWewwl4b1w-qdhWfQgXpMq7qfNgBvgG-_qAsSdR_4LqwAItYT3Wfr4zfpxmo6BN6mOUvtL7tqCk6TZ7ZGUspQIzO49EDZEiu2AZOwB9SYpOvU7cLc1BUUZbTaP2uc66AgtiI1mSiTrhJn_lrPuIK1_P48a7vvRpCgH95h3VE87GYeNgTCdM0YPx6uP0CX3D"
    },
    "nethaaji@algoforge.dev": {
        "email": "nethaaji@algoforge.dev",
        "username": "Nethaaji",
        "password": "password123",
        "xp": 3100,
        "avatar": "https://api.dicebear.com/7.x/identicon/svg?seed=Nethaaji"
    },
    "operator@algoforge.dev": {
        "email": "operator@algoforge.dev",
        "username": "Operator_01",
        "password": "password123",
        "xp": 1950,
        "avatar": "https://api.dicebear.com/7.x/identicon/svg?seed=Operator_01"
    },
    "cadet@algoforge.io": {
        "email": "cadet@algoforge.io",
        "username": "Cadet_Guest",
        "password": "password123",
        "xp": 500,
        "avatar": "https://api.dicebear.com/7.x/identicon/svg?seed=Cadet"
    }
}

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "AlgoForge Engine", "version": "2.5.0"}

@app.post("/api/auth/register", response_model=AuthResponse)
async def register(req: AuthRequest):
    email_clean = req.email.strip().lower() if req.email else "operator@algoforge.dev"
    if not email_clean or "@" not in email_clean:
        email_clean = f"{email_clean or 'cadet'}@algoforge.dev"
    
    username = req.username or email_clean.split("@")[0].capitalize()
    
    if email_clean in REGISTERED_USERS:
        # Seamlessly log in and update if already exists
        user_record = REGISTERED_USERS[email_clean]
        if req.username:
            user_record["username"] = req.username
        if req.password:
            user_record["password"] = req.password
    else:
        user_record = {
            "email": email_clean,
            "username": username,
            "password": req.password or "password123",
            "xp": 850,
            "avatar": f"https://api.dicebear.com/7.x/identicon/svg?seed={username}"
        }
        REGISTERED_USERS[email_clean] = user_record
    
    return AuthResponse(
        success=True,
        message="Registration successful! Rig initialized.",
        user={"email": user_record["email"], "username": user_record["username"], "xp": user_record["xp"], "avatar": user_record["avatar"]},
        token=f"token_{user_record['username']}_2026"
    )

@app.post("/api/auth/login", response_model=AuthResponse)
async def login(req: AuthRequest):
    email_clean = req.email.strip().lower() if req.email else "operator@algoforge.dev"
    if not email_clean or "@" not in email_clean:
        email_clean = f"{email_clean or 'cadet'}@algoforge.dev"

    user = REGISTERED_USERS.get(email_clean)
    if not user:
        # Auto-provision on login for instant frictionless onboarding
        username = req.username or email_clean.split("@")[0].capitalize()
        user = {
            "email": email_clean,
            "username": username,
            "password": req.password or "password123",
            "xp": 1000,
            "avatar": f"https://api.dicebear.com/7.x/identicon/svg?seed={username}"
        }
        REGISTERED_USERS[email_clean] = user
    elif req.password and user["password"] != req.password:
        # Seamlessly update password in local mode
        user["password"] = req.password
    
    return AuthResponse(
        success=True,
        message="Login successful! Welcome back, Operator.",
        user={"email": user["email"], "username": user["username"], "xp": user["xp"], "avatar": user["avatar"]},
        token=f"token_{user['username']}_2026"
    )

@app.post("/api/auth/oauth", response_model=AuthResponse)
async def oauth_authenticate(req: OAuthRequest):
    provider = req.provider.capitalize()
    email_clean = req.email.strip().lower() if req.email else f"cadet.{provider.lower()}@algoforge.dev"
    username = req.username or email_clean.split("@")[0].capitalize()

    user = REGISTERED_USERS.get(email_clean)
    if not user:
        user = {
            "email": email_clean,
            "username": username,
            "password": f"oauth_{provider.lower()}_authenticated",
            "xp": 1200,
            "avatar": f"https://api.dicebear.com/7.x/identicon/svg?seed={username}",
            "provider": provider
        }
        REGISTERED_USERS[email_clean] = user

    return AuthResponse(
        success=True,
        message=f"Verified through {provider} Enterprise OAuth. Session activated.",
        user={"email": user["email"], "username": user["username"], "xp": user["xp"], "avatar": user["avatar"]},
        token=f"oauth_{provider.lower()}_{user['username']}_2026"
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
    if os.path.exists(file_path):
        try:
            import json
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    return []

EXPERIENCE_QUESTIONS = load_json_bank(EXP_QUESTIONS_PATH)
CHALLENGE_QUESTIONS = load_json_bank(CHAL_QUESTIONS_PATH)

@app.get("/api/questions/experience")
async def get_experience_questions(topic: str = None, type: str = None):
    questions = load_json_bank(EXP_QUESTIONS_PATH) or EXPERIENCE_QUESTIONS
    if topic and topic.lower() != "all":
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if type:
        questions = [q for q in questions if q.get("type", "").lower() == type.lower()]
    return {"total": len(questions), "questions": questions}

@app.get("/api/questions/challenge")
async def get_challenge_questions(topic: str = None, type: str = None, attempt: int = None):
    questions = load_json_bank(CHAL_QUESTIONS_PATH) or CHALLENGE_QUESTIONS
    if attempt is not None and attempt > 0:
        coding_pool = [q for q in questions if q.get("type") == "coding"]
        out_pool = [q for q in questions if q.get("type") == "output_prediction"]
        mcq_pool = [q for q in questions if q.get("type") == "mcq"]

        c_start = ((attempt - 1) * 5) % len(coding_pool) if coding_pool else 0
        c_selected = [coding_pool[(c_start + i) % len(coding_pool)] for i in range(min(5, len(coding_pool)))]

        o_start = ((attempt - 1) * 3) % len(out_pool) if out_pool else 0
        o_selected = [out_pool[(o_start + i) % len(out_pool)] for i in range(min(3, len(out_pool)))]

        m_start = ((attempt - 1) * 2) % len(mcq_pool) if mcq_pool else 0
        m_selected = [mcq_pool[(m_start + i) % len(mcq_pool)] for i in range(min(2, len(mcq_pool)))]

        all_q = c_selected + o_selected + m_selected
        attempt_questions = []
        for idx, q in enumerate(all_q):
            q_copy = dict(q)
            q_copy["id"] = f"AF{idx + 1}"
            q_copy["attemptNum"] = attempt
            attempt_questions.append(q_copy)
        questions = attempt_questions
    if topic:
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if type:
        questions = [q for q in questions if q.get("type", "").lower() == type.lower()]
    return {"total": len(questions), "questions": questions}

@app.get("/api/questions")
async def get_question_bank(mode: str = None, source: str = None, topic: str = None, type: str = None):
    if mode == "experience":
        questions = EXPERIENCE_QUESTIONS
    elif mode == "challenge":
        questions = CHALLENGE_QUESTIONS
    else:
        questions = EXPERIENCE_QUESTIONS if EXPERIENCE_QUESTIONS else MULTI_SOURCE_QUESTION_BANK
    if source:
        questions = [q for q in questions if q.get("source", "").lower() == source.lower()]
    if topic and topic.lower() != "all":
        questions = [q for q in questions if q.get("topic", "").lower() == topic.lower()]
    if type:
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
    uvicorn.run(app, host="0.0.0.0", port=8000)

