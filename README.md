# AlgoForge — Dual-Engine Algorithmic Platform

AlgoForge is a dual-engine algorithmic learning and competitive verification platform featuring step-by-step state animations in **Experience Mode** and LeetCode-style timed coding challenges with sub-millisecond hardware telemetry in **Challenge Mode**.

---

## 🚀 Instant Deployment with GitHub Pages

This repository is pre-configured for zero-setup deployment via **GitHub Pages**:

1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Deploy AlgoForge to GitHub Pages"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

2. Go to your repository on GitHub:
   - Click **Settings** → **Pages** (in the left sidebar).
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Select branch: `main` and folder: `/ (root)`.
   - Click **Save**.

3. Your website will be live in ~1 minute at:
   `https://<your-username>.github.io/<your-repo-name>/`

---

## 📂 Repository Structure

- `index.html` — Main production web application entry point (GitHub Pages root).
- `app.js` — Core client-side execution, telemetry profiler, question bank manager, and interactive UI logic.
- `styles.css` — Custom utility and animation styles.
- `AlgoForge_Challenge_Mode_Question_Bank.json` — 36 curated challenge questions across Sorting, Trees, Graphs, and DP.
- `AlgoForge_Experience_Mode_Question_Bank.json` — 24 visualizer problem sets with state trace timelines.
- `backend/` — Optional Python FastAPI backend for server-side code execution and API telemetry.
- `frontend/` — Mirrored frontend workspace files.

---

## 💻 Local Development

To run locally with the FastAPI backend:

```bash
# 1. Install dependencies
pip install -r backend/requirements.txt

# 2. Start the Uvicorn server
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload
```

Open `http://localhost:8080` in your web browser.
