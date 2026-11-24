import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', encoding='utf-8') as f_in:
    lines = f_in.readlines()
for i, l in enumerate(lines[4500:4580], 4501):
    print(f'{i}: {l}', end='')
