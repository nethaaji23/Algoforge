import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'tabletFilterPills' in l or 'tablet-filter-btn' in l:
        print(f"{i+1}: {l.strip()[:100]}")
