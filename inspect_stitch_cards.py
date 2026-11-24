import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/stitch_perf_screen.html', encoding='utf-8') as f:
    stitch = f.read()

# Let's extract all sections / major divs
matches = list(re.finditer(r'<div class="[^"]*rounded-\[24px\][^"]*"', stitch))
for i, m in enumerate(matches):
    start = m.start()
    sample = stitch[start:start+400]
    sample_clean = re.sub(r'\s+', ' ', sample)
    print(f"=== Card {i} ===")
    print(sample_clean)
