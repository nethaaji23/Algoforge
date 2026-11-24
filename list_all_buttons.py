import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

buttons = []
for m in re.finditer(r'<button\b([^>]*)>(.*?)</button>', html, re.DOTALL | re.IGNORECASE):
    attrs = m.group(1)
    content = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    content = re.sub(r'\s+', ' ', content)
    id_m = re.search(r'id=["\']([^"\']+)["\']', attrs)
    class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
    buttons.append({
        'id': id_m.group(1) if id_m else None,
        'content': content[:45],
        'class': class_m.group(1) if class_m else ''
    })

import sys
sys.stdout.reconfigure(encoding='utf-8')
for i, b in enumerate(buttons):
    print(f"{i+1:2d}. ID: {str(b['id']):30s} | Content: {b['content']}")
