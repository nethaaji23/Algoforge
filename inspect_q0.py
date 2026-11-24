import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/challenge_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(json.dumps(questions[0], indent=2))
