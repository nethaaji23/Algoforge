import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/frontend/app.js', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'renderDynamicBarChart' in l or 'renderScoreProgressionGraph' in l or 'initPerformanceDashboard' in l or 'renderPerformance' in l:
        print(f'{i+1}: {l.strip()[:100]}')
