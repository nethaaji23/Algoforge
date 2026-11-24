import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\netha\.gemini\antigravity\scratch\algoforge_hyper_glitch\frontend\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'tablet-filter' in l or 'exp-filter' in l or 'Easy' in l or 'Medium' in l or 'Hard' in l or 'tablet-diff' in l:
        print(f'{i+1}: {l.strip()[:100]}')
