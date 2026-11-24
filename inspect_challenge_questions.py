import re

path = r"C:\Users\netha\.gemini\antigravity\scratch\algoforge_hyper_glitch\frontend\app.js"
with open(path, "r", encoding="utf-8") as f:
    js = f.read()

start = js.find("let CHALLENGE_EXAM_QUESTION_BANK = [")
end = js.find("let EXP_PRACTICE_QUESTIONS = [")
chunk = js[start:end]

questions = re.findall(r'\{\s*id:\s*"([^"]+)",\s*source:\s*"([^"]+)",[\s\S]*?title:\s*"([^"]+)"', chunk)
print(f"Found {len(questions)} questions:")
for i, (qid, src, title) in enumerate(questions):
    print(f"  {i+1}. id={qid} | src={src} | title={title}")
