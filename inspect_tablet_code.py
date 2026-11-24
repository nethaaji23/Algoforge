import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/app.js', encoding='utf-8') as f:
    lines = f.readlines()

print("--- renderExperienceQuestionTablet (lines 7220-7275) ---")
for i in range(7215, 7275):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- renderQuestionTablet (lines 7650-7715) ---")
for i in range(7650, 7715):
    print(f"{i+1}: {lines[i]}", end="")
