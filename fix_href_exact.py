with open('index.html', 'r') as f:
    html = f.read()

broken_1 = '西敏寺與大笨鐘 <span class="ml-1 text-[11px] bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded border border-blue-200">大人 £31 / 小孩 £14</span>+London'
fixed_1 = '西敏寺與大笨鐘+London'
html = html.replace(broken_1, fixed_1)

broken_2 = '千禧橋 <span class="ml-1 text-[11px] bg-green-100 text-green-700 px-1.5 py-0.5 rounded border border-green-200">Free</span> 與聖保羅大教堂 <span class="ml-1 text-[11px] bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded border border-blue-200">大人 £29.7 / 小孩 £11.5</span>+London'
fixed_2 = '千禧橋與聖保羅大教堂+London'
html = html.replace(broken_2, fixed_2)

with open('index.html', 'w') as f:
    f.write(html)
