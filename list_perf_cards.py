import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f_in:
    lines = f_in.readlines()
for i, l in enumerate(lines[3455:4850], 3456):
    s = l.strip()
    if '<h2' in s or '<h3' in s or 'id="perf-' in s:
        print(f'{i}: {s[:100]}')
