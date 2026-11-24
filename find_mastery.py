import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f_in:
    lines = f_in.readlines()
for i, l in enumerate(lines[3455:4850], 3456):
    if 'concept' in l.lower() or 'master' in l.lower() or 'develop' in l.lower():
        print(f'{i}: {l.strip()[:100]}')
