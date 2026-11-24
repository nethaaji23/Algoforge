import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'settings' in l.lower() or 'navigation' in l.lower() or 'nav-status' in l.lower():
        print(f"{i+1}: {l.strip()[:100]}")
