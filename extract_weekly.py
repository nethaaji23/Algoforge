import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/stitch_perf_screen.html', encoding='utf-8') as f:
    stitch = f.read()

# Find Weekly Execution & Latency Trends in stitch
m = re.search(r'Weekly Execution &amp; Latency Trends.*?</svg>\s*</div>\s*</div>\s*</div>', stitch, re.DOTALL)
if m:
    print("Found section snippet length:", len(m.group(0)))
    with open('stitch_weekly_snippet.html', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Wrote stitch_weekly_snippet.html")
else:
    print("Not found with regex, let's search broader")
