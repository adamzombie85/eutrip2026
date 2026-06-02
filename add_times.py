import os
import re

md_path = 'UK_Trip_Itinerary_V2.md'
html_path = 'index.html'

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# First, fix the order for Day 2, Day 6, Day 7 so they are chronological
# Day 2 swap
day2_p2 = """*   **行程點 2：聖詹姆士公園 (St James's Park)**
    *   **建議停留時間**：1.5 小時 (含野餐)
    *   **必逛看點**：公園內有超多不怕人的松鼠、天鵝與大鵜鶘！小孩絕對會愛死，讓小孩嘗試用英文問路人動物的名字。中午找一片舒適的草地享用超市買來的 Meal Deal。全家散步走到湖邊橋上，拍下白金漢宮的遠景。"""
day2_p3 = """*   **行程點 3：白金漢宮衛兵交接**
    *   **建議停留時間**：1.5 小時
    *   **必逛看點**：在林蔭大道 (The Mall) 或威靈頓軍營觀看交接儀式，避開正門人擠人。媽媽必拍的英倫風情與騎兵帥氣身影；小孩可觀察衛兵的毛毛帽 (熊皮帽) 和樂隊演奏曲目；爸爸可解說皇家衛兵的歷史傳統。"""
new_day2_p2 = day2_p3.replace("行程點 3", "行程點 2")
new_day2_p3 = day2_p2.replace("行程點 2", "行程點 3")
md_content = md_content.replace(day2_p2 + "\n" + day2_p3, new_day2_p2 + "\n" + new_day2_p3)

# Day 6 swap
day6_p2 = """*   **行程點 2：康河撐篙 (Punting)**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：互動性高，小孩會覺得像坐船探險。聽著年輕的大學生船夫用英文講解劍橋歷史 (可請爸爸翻譯)。沿途穿梭嘆息橋與數學橋，可以讓小孩找找看河裡有沒有鴨子，享受英倫大學城獨特的悠閒水上時光。"""
day6_p3 = """*   **行程點 3：劍橋草地野餐**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：自備三明治與超市買的點心，在劍橋大片綠地上野餐。讓小孩盡情奔跑放風，爸爸可以趁機吃滿自備的生菜沙拉。一家人躺在草地上看著古老建築與藍天，享受遠離倫敦市區的平靜。"""
new_day6_p2 = day6_p3.replace("行程點 3", "行程點 2")
new_day6_p3 = day6_p2.replace("行程點 2", "行程點 3")
md_content = md_content.replace(day6_p2 + "\n" + day6_p3, new_day6_p2 + "\n" + new_day6_p3)

# Day 7 swap
day7_p2 = """*   **行程點 2：巴斯 (Bath) 羅馬浴場與市區**
    *   **建議停留時間**：3 小時
    *   **必逛看點**：爸爸必看古羅馬浴場遺跡，並用專屬語音導覽 (有兒童版！) 讓小孩聽羅馬人的泡澡故事。接著逛巴斯市區，欣賞新月樓與圓形廣場。巴斯的蜜糖色石灰岩建築拍起來極美 (媽媽愛死)。若時間充裕，可聽街頭藝人演奏。"""
day7_p3 = """*   **行程點 3：Sally Lunn's 圓麵包**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：前往巴斯最古老的房屋，品嚐著名的 Sally Lunn's 傳統下午茶巨型圓麵包 (Bunn)。媽媽的美食清單必打卡，小孩會對比臉還大的麵包感到驚奇。全家點一份甜的、一份鹹的分食，享受英式下午茶時光。"""
new_day7_p2 = day7_p3.replace("行程點 3", "行程點 2")
new_day7_p3 = day7_p2.replace("行程點 2", "行程點 3")
md_content = md_content.replace(day7_p2 + "\n" + day7_p3, new_day7_p2 + "\n" + new_day7_p3)


times = [
    # Day 1
    "16:00", "17:45", "19:45",
    # Day 2
    "09:15", "10:15", "12:00",
    # Day 3
    "09:30", "13:00", "16:30",
    # Day 4
    "10:00", "14:30", "16:30",
    # Day 5
    "10:30", "12:45", "15:45",
    # Day 6
    "10:00", "12:00", "13:00",
    # Day 7
    "10:30", "13:30", "14:30",
    # Day 8
    "09:30", "12:15", "14:45"
]

time_idx = 0
new_md_lines = []
for line in md_content.split('\n'):
    new_md_lines.append(line)
    if "**建議停留時間**：" in line:
        # Insert time before this line
        time_str = times[time_idx]
        new_md_lines.insert(-1, f"    *   **建議開始時間**：{time_str}")
        time_idx += 1

with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_md_lines))


# Now update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace("停留: ", "停留 ")

# Swap in HTML Day 2
day2_html_p2 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/St+James+Park+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">聖詹姆士公園 (St James's Park) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>公園內有超多不怕人的松鼠、天鵝與大鵜鶘！小孩絕對會愛死，讓小孩嘗試用英文問路人動物的名字。中午找一片舒適的草地享用超市買來的 Meal Deal。全家散步走到湖邊橋上，拍下白金漢宮的遠景。</p>
                                </li>"""
day2_html_p3 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Changing+of+the+Guard+The+Mall+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">白金漢宮衛兵交接 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>在林蔭大道 (The Mall) 或威靈頓軍營觀看交接儀式，避開正門人擠人。媽媽必拍的英倫風情與騎兵帥氣身影；小孩可觀察衛兵的毛毛帽 (熊皮帽) 和樂隊演奏曲目；爸爸可解說皇家衛兵的歷史傳統。</p>
                                </li>"""
# we need to fix dot colors to maintain order (cyan, blue, purple)
new_day2_html_p2 = day2_html_p3.replace("bg-purple-500", "bg-blue-500")
new_day2_html_p3 = day2_html_p2.replace("bg-blue-500", "bg-purple-500")
html_content = html_content.replace(day2_html_p2 + "\n" + day2_html_p3, new_day2_html_p2 + "\n" + new_day2_html_p3)

# Swap Day 6
day6_html_p2 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">康河撐篙 (Punting)</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>互動性高，小孩會覺得像坐船探險。聽著年輕的大學生船夫用英文講解劍橋歷史 (可請爸爸翻譯)。沿途穿梭嘆息橋與數學橋，可以讓小孩找找看河裡有沒有鴨子，享受英倫大學城獨特的悠閒水上時光。</p>
                                </li>"""
day6_html_p3 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">劍橋草地野餐</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>自備三明治與超市買的點心，在劍橋大片綠地上野餐。讓小孩盡情奔跑放風，爸爸可以趁機吃滿自備的生菜沙拉。一家人躺在草地上看著古老建築與藍天，享受遠離倫敦市區的平靜。</p>
                                </li>"""
new_day6_html_p2 = day6_html_p3.replace("bg-purple-500", "bg-blue-500")
new_day6_html_p3 = day6_html_p2.replace("bg-blue-500", "bg-purple-500")
html_content = html_content.replace(day6_html_p2 + "\n" + day6_html_p3, new_day6_html_p2 + "\n" + new_day6_html_p3)

# Swap Day 7
day7_html_p2 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">巴斯 (Bath) 羅馬浴場與市區</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 3 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>爸爸必看古羅馬浴場遺跡，並用專屬語音導覽 (有兒童版！) 讓小孩聽羅馬人的泡澡故事。接著逛巴斯市區，欣賞新月樓與圓形廣場。巴斯的蜜糖色石灰岩建築拍起來極美 (媽媽愛死)。若時間充裕，可聽街頭藝人演奏。</p>
                                </li>"""
day7_html_p3 = """                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Sally Lunn's 圓麵包</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>前往巴斯最古老的房屋，品嚐著名的 Sally Lunn's 傳統下午茶巨型圓麵包 (Bunn)。媽媽的美食清單必打卡，小孩會對比臉還大的麵包感到驚奇。全家點一份甜的、一份鹹的分食，享受英式下午茶時光。</p>
                                </li>"""
new_day7_html_p2 = day7_html_p3.replace("bg-purple-500", "bg-blue-500")
new_day7_html_p3 = day7_html_p2.replace("bg-blue-500", "bg-purple-500")
html_content = html_content.replace(day7_html_p2 + "\n" + day7_html_p3, new_day7_html_p2 + "\n" + new_day7_html_p3)


# Add times to HTML
time_idx = 0
def replace_time(match):
    global time_idx
    time_str = times[time_idx]
    time_idx += 1
    duration_html = match.group(0)
    # <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留 1 小時</span>
    duration_text = re.search(r'>([^<]+)</span>', duration_html).group(1)
    
    new_html = f'<div class="flex gap-1"><span class="text-[10px] bg-blue-100 text-blue-700 px-2 py-0.5 rounded-full border border-blue-200 font-bold">{time_str}</span><span class="text-[10px] bg-gray-100 text-gray-600 px-2 py-0.5 rounded-full border border-gray-200">{duration_text}</span></div>'
    return new_html

html_content = re.sub(r'<span class="text-\[10px\] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留[^<]+</span>', replace_time, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Processed {time_idx} times.")
