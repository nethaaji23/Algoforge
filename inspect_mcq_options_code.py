import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- Challenge MCQ Options (lines 7745-7790) ---")
for i in range(7740, 7780):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- Experience MCQ Options (lines 7315-7360) ---")
for i in range(7312, 7350):
    print(f"{i+1}: {lines[i]}", end="")
