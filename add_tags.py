with open('index.html', 'r') as f:
    html = f.read()

free_tag = '<span class="ml-1 text-[11px] bg-green-100 text-green-700 px-1.5 py-0.5 rounded border border-green-200">Free</span>'
book_tag = '<span class="ml-1 text-[11px] bg-orange-100 text-orange-700 px-1.5 py-0.5 rounded border border-orange-200">Book</span>'

def price_tag(adult, child):
    return f'<span class="ml-1 text-[11px] bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded border border-blue-200">大人 {adult} / 小孩 {child}</span>'

replacements = {
    '倫敦塔橋 (Tower Bridge)': '倫敦塔橋 (Tower Bridge)' + price_tag('£18', '£9'),
    '西敏寺與大笨鐘': '西敏寺與大笨鐘 ' + price_tag('£31', '£14'),
    '衛兵交接 (The Mall)': '衛兵交接 (The Mall) ' + free_tag,
    '自然史博物館 (需預約)': '自然史博物館 ' + free_tag + book_tag,
    '科學博物館 & Wonderlab': '科學博物館 ' + free_tag + book_tag + ' & Wonderlab',
    '大英博物館 (免費，需預約)': '大英博物館 ' + free_tag + book_tag,
    '柯芬園 & Neil\'s Yard': '柯芬園 & Neil\'s Yard ' + free_tag,
    '波羅市場 Borough Market': '波羅市場 Borough Market ' + free_tag,
    '泰特現代藝術館 (Tate Modern)': '泰特現代藝術館 (Tate Modern) ' + free_tag,
    '千禧橋與聖保羅大教堂': '千禧橋 ' + free_tag + ' 與聖保羅大教堂 ' + price_tag('£29.7', '£11.5'),
    '國王學院與食屍鬼鐘': '國王學院 ' + price_tag('£18', '£15') + ' 與食屍鬼鐘 ' + free_tag,
    '康河撐篙 (Punting)': '康河撐篙 (Punting) ' + price_tag('約£20', '約£15'),
    '豪華早午餐：Darwin Brasserie': '豪華早午餐：Darwin Brasserie ' + book_tag,
    'Leadenhall Market': 'Leadenhall Market ' + free_tag,
    'Museum of London Docklands': 'Museum of London Docklands ' + free_tag,
    '倫敦塔 (付費門票)': '倫敦塔 ' + price_tag('£37', '£18.5')
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
