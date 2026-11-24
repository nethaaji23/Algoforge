import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[:1000]):
    if '<body' in l or '<header' in l:
        print(f"{i+1}: {l.strip()[:90]}")
