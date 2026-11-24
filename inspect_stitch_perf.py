import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\netha\.gemini\antigravity\scratch\algoforge_hyper_glitch\stitch_perf_screen.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx2 = html.find('Active Telemetry &amp; Bottleneck Feeds')
if idx2 != -1:
    print('=== Active Telemetry & Bottleneck Feeds in Stitch ===')
    print(html[idx2-200:idx2+2500])
