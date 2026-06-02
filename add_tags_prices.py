import os
import re

md_path = 'UK_Trip_Itinerary_V2.md'
html_path = 'index.html'

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

activities = [
    ("Airbnb 放置行李與周邊熟悉", "免費", ""),
    ("倫敦塔橋 (Tower Bridge) 看夜景", "免費", ""),
    ("Sainsbury's 超市採買晚餐", "免費", ""),
    ("大笨鐘與西敏寺 (外觀)", "免費", ""),
    ("白金漢宮衛兵交接", "免費", ""),
    ("聖詹姆士公園 (St James's Park)", "免費", ""),
    ("自然史博物館", "免費", " (雖然免費，但強烈建議官網事先預約入場時段免排隊)"),
    ("科學博物館 (含 Wonderlab)", "事先預約", " 💡 **票價資訊**：Wonderlab 大人 £11 / 小孩 £11"),
    ("Harrods 貴婦百貨", "免費", ""),
    ("大英博物館", "免費", " (雖然免費，但強烈建議官網事先預約入場時段免排隊)"),
    ("牛津街 (Oxford Street)", "免費", ""),
    ("柯芬園 (Covent Garden)", "免費", ""),
    ("Borough Market (波羅市場)", "免費", ""),
    ("HMS Belfast (貝爾法斯特號軍艦)", "事先預約", " 💡 **票價資訊**：大人 £25.45 / 小孩 £12.70"),
    ("千禧橋與南岸漫步", "免費", ""),
    ("劍橋國王學院與校園漫步", "現場購票", " 💡 **票價資訊**：國王學院大人 £15 / 小孩 £11.50"),
    ("康河撐篙 (Punting)", "現場購票", " 💡 **票價資訊**：船票大人約 £25 / 小孩約 £15"),
    ("劍橋草地野餐", "免費", ""),
    ("巨石陣 (Stonehenge)", "事先預約", " 💡 **票價資訊**：大人 £26 / 小孩 £16"),
    ("巴斯 (Bath) 羅馬浴場與市區", "事先預約", " 💡 **票價資訊**：羅馬浴場大人 £28 / 小孩 £20"),
    ("Sally Lunn's 圓麵包", "現場購票", " 💡 **票價資訊**：餐點低消大人約 £12 / 小孩約 £8"),
    ("倫敦塔 (Tower of London)", "事先預約", " 💡 **票價資訊**：大人 £34.80 / 小孩 £17.40"),
    ("Sky Garden (空中花園) 景觀大餐", "事先預約", " 💡 **票價資訊**：景觀餐廳低消大人約 £35 / 小孩無限制"),
    ("Spitalfields City Farm", "免費", ""),
]

# For markdown, we replace the titles and descriptions
for title, tag, desc_add in activities:
    # 1. Add tag to title in MD
    # Match: *   **行程點 1：Airbnb 放置行李與周邊熟悉**
    # or *   **行程點 1：Airbnb 放置行李與周邊熟悉**
    md_content = re.sub(r'(\*\s+\*\*行程點 \d+：' + re.escape(title) + r'\*\*)', r'\1 【' + tag + r'】', md_content)
    
    # 2. Add description to MD
    # We find the block for this title, and then append the desc_add to the "必逛看點" line
    # Find the title index
    idx = md_content.find("："+title+"**")
    if idx != -1:
        # Find next "必逛看點"
        highlight_idx = md_content.find("**必逛看點**：", idx)
        if highlight_idx != -1:
            end_of_line = md_content.find("\n", highlight_idx)
            if end_of_line != -1:
                # Insert desc_add before the newline
                md_content = md_content[:end_of_line] + desc_add + md_content[end_of_line:]

    # 3. Add tag to HTML
    html_tag_class = ""
    if tag == "免費":
        html_tag_class = "bg-green-100 text-green-700 border-green-200"
    elif tag == "現場購票":
        html_tag_class = "bg-orange-100 text-orange-700 border-orange-200"
    elif tag == "事先預約":
        html_tag_class = "bg-red-100 text-red-700 border-red-200"
        
    tag_html = f'<span class="ml-1 px-1.5 py-0.5 rounded text-[10px] font-normal border {html_tag_class}">{tag}</span>'
    
    # We find <p class="font-bold text-sm">...TITLE...</p>
    # and insert tag_html right before </p>
    # We must be careful to only replace the first occurrence that matches the title
    # Let's use regex with a lookahead or just find all <p class="font-bold text-sm"> and check if it contains the title
    p_pattern = re.compile(r'<p class="font-bold text-sm">(.*?)</p>')
    matches = p_pattern.finditer(html_content)
    for match in matches:
        inner_html = match.group(1)
        if title in inner_html and "ml-1 px-1.5 py-0.5" not in inner_html: # avoid double adding
            # Add tag before </p>
            replacement = f'<p class="font-bold text-sm flex items-center flex-wrap">{inner_html} {tag_html}</p>'
            html_content = html_content[:match.start()] + replacement + html_content[match.end():]
            break
            
    # 4. Add description to HTML
    # HTML description looks like: <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>...DESC...</p>
    # It is exactly below the title p block.
    # Actually, we can just find the title block index, then find the next "<strong>活動：</strong>", then find "</p>" and insert desc_add before it.
    title_idx = html_content.find(title)
    if title_idx != -1:
        activity_idx = html_content.find("<strong>活動：</strong>", title_idx)
        if activity_idx != -1 and activity_idx - title_idx < 1000: # Ensure it's the right activity
            end_p_idx = html_content.find("</p>", activity_idx)
            if end_p_idx != -1:
                # Need to convert markdown bold to HTML bold for the desc_add
                desc_html = desc_add.replace("**票價資訊**：", "<strong>票價資訊：</strong>")
                html_content = html_content[:end_p_idx] + desc_html + html_content[end_p_idx:]


with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Added tags and prices to MD and HTML.")
