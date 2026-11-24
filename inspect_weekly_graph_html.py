import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[3960:4040], 3961):
    print(f'{i}: {l}', end='')
