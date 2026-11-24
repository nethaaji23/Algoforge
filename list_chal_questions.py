import sys, json
sys.stdout.reconfigure(encoding='utf-8')
with open('AlgoForge_Challenge_Mode_Question_Bank.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx, q in enumerate(data):
    print(f"{q['id']}: {q['title']} (current diff: {q.get('difficulty')})")
