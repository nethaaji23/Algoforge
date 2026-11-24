import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- Experience Mode Header Banner (lines 2460-2480) ---")
for i in range(2460, 2480):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- Challenge Mode Header Banner (lines 3070-3090) ---")
for i in range(3068, 3088):
    print(f"{i+1}: {lines[i]}", end="")
