import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/stitch_perf_screen.html', encoding='utf-8') as f:
    content = f.read()

print("File length:", len(content))
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL)
print("\n--- Headings ---")
for h in headings:
    cleaned = re.sub(r'<[^>]+>', '', h).strip()
    print("-", cleaned)

cards = re.findall(r'<div[^>]*rounded-\[24px\][^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
print(f"\n--- Found {len(cards)} main rounded-[24px] cards ---")
