import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\netha\.gemini\antigravity\scratch\algoforge_hyper_glitch\frontend\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(3860, 3950):
    print(f'{i+1}: {lines[i]}', end='')
