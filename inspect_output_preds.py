import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in [
    'AlgoForge_Experience_Mode_Question_Bank.json',
    'experience_questions.json',
    'AlgoForge_Challenge_Mode_Question_Bank.json',
    'challenge_questions.json',
    'backend/dataset.py'
]:
    path = f'C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/{fname}'
    print(f"\n=================== {fname} ===================")
    if fname.endswith('.json'):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        questions = data.get('questions', data) if isinstance(data, dict) else data
        print(f"Total: {len(questions)}")
        for q in questions:
            q_type = q.get('type')
            sub_type = q.get('subtype') or q.get('category') or q.get('mode')
            title = q.get('title')
            qid = q.get('id')
            if 'output' in str(q).lower() or q_type == 'output_prediction':
                print(f"  [{qid}] type={q_type}, title={title}")
    elif fname.endswith('.py'):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for line in content.splitlines():
            if 'output_prediction' in line or 'output prediction' in line.lower():
                print("  ", line.strip()[:100])
