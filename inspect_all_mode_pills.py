import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'MODE //' in l:
        print(f"--- Line {i+1} ---")
        for j in range(max(0, i-4), min(len(lines), i+4)):
            print(f"{j+1}: {lines[j]}", end="")
