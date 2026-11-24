import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/stitch_perf_screen.html', encoding='utf-8') as f:
    stitch = f.read()

idx = stitch.find("Current Test Rig")
if idx != -1:
    print(stitch[idx-100:idx+800])
