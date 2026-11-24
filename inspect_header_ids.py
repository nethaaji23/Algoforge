import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[:100]):
    if 'header' in l.lower() or 'nav' in l.lower() or 'id=' in l:
        print(f"{i+1}: {l.strip()[:90]}")
