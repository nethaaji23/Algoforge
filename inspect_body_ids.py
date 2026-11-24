import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[100:200], 101):
    if 'id=' in l or '<body' in l or '<header' in l:
        print(f"{i}: {l.strip()[:90]}")
