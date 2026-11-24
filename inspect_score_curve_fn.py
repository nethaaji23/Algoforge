import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/app.js', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[2700:2780], 2701):
    print(f'{i}: {l}', end='')
