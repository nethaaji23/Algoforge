import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/stitch_perf_screen.html', encoding='utf-8') as f:
    stitch = f.read()

idx = stitch.find("Weekly Execution")
print("Index:", idx)
if idx != -1:
    snippet = stitch[idx-200:idx+2500]
    print(snippet[:600])
    with open('stitch_weekly_full.html', 'w', encoding='utf-8') as out:
        out.write(stitch[idx-300:idx+4500])
