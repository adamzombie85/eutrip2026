import os
import re

md_path = 'UK_Trip_Itinerary_V2.md'
html_path = 'index.html'

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Update Markdown
old_md_checklist = """## ⚠️ 預約檢查清單
- [ ] **出發前 3 個月**：預訂前往 Salisbury (巨石陣轉乘點) 與 Bath (巴斯) 的火車票 (使用 Family & Friends Railcard)。
- [ ] **出發前 1 個月**：預約大英博物館免費時段、購買巨石陣與巴斯浴場門票。
- [ ] **出發前 3 週**：搶 Sky Garden 免費景觀台門票 (這是保留給全家吃頓好的重要行程，必搶！)。"""

new_md_checklist = """## ⚠️ 預約檢查清單
- [ ] **出發前 3 個月 (或機票確認後)**：購買 Family & Friends Railcard，並預訂前往劍橋、Salisbury (巨石陣) 與 Bath (巴斯) 的早鳥火車票。
- [ ] **出發前 2 個月 (60天前)**：預約 **Sky Garden 的 Darwin Brasserie 景觀餐廳** (極度熱門，務必第一時間搶訂，訂到直接免搶門票)。
- [ ] **出發前 1 個月**：購買 **巨石陣 (Stonehenge)** 與 **巴斯羅馬浴場** 門票。
- [ ] **出發前 3~4 週**：預約 **大英博物館**、**自然史博物館** 免費入場時段，購買 **科學博物館 Wonderlab** 門票。
- [ ] **出發前 1~2 週**：購買 **倫敦塔 (Tower of London)** 與 **HMS Belfast 貝爾法斯特號軍艦** 門票 (線上先買省去現場買票排隊)。"""

if old_md_checklist in md_content:
    md_content = md_content.replace(old_md_checklist, new_md_checklist)
else:
    print("Could not find exact MD checklist, trying regex.")
    # fallback regex
    md_content = re.sub(r'## ⚠️ 預約檢查清單.*?(?=\n\n|\Z)', new_md_checklist, md_content, flags=re.DOTALL)


# Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# The HTML block to replace is inside <div id="tab-checklist"
start_idx = html_content.find('<div id="tab-checklist"')
if start_idx != -1:
    block_start = html_content.find('<div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-5 mb-4">', start_idx)
    if block_start != -1:
        # Find the matching closing div for this block
        # We know it ends before the next <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-5"> (the supermarket one)
        next_block = html_content.find('<div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-5">', block_start + 1)
        if next_block != -1:
            old_html_block = html_content[block_start:next_block]
            
            new_html_block = """<div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-5 mb-4">
                <h3 class="font-bold text-red-600 mb-3"><i class="fa-solid fa-clock mr-2"></i>行前預約與死線</h3>
                <div class="space-y-4">
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">申辦海外神卡 & Railcard 綁定</span>
                            <span class="text-xs text-gray-500 block">星展 eco 等海外高回饋卡、下載 Railcard APP 綁定</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 機票確定後盡快處理</span>
                        </div>
                    </label>
                    <div class="border-b border-gray-100"></div>
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">早鳥火車票 (劍橋 / 巴斯 / 巨石陣)</span>
                            <span class="text-xs text-gray-500 block">Advance 早鳥票，搭配 Family & Friends Railcard 最省</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 出發前 2.5 ~ 3 個月 (早鳥釋出即買)</span>
                        </div>
                    </label>
                    <div class="border-b border-gray-100"></div>
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">Darwin Brasserie 景觀餐廳 (Sky Garden)</span>
                            <span class="text-xs text-gray-500 block">超級熱門！有預約餐廳即可免搶票直接登頂</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 出發前 60 天 (開放即搶)</span>
                        </div>
                    </label>
                    <div class="border-b border-gray-100"></div>
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">巨石陣 & 巴斯羅馬浴場門票</span>
                            <span class="text-xs text-gray-500 block">熱門郊區景點，為確保入場需提早買妥</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 出發前 1 個月</span>
                        </div>
                    </label>
                    <div class="border-b border-gray-100"></div>
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">三大博物館門票 (大英/自然史/科學)</span>
                            <span class="text-xs text-gray-500 block">大英/自然史預約免費時段，科學館加購 Wonderlab</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 出發前 3~4 週</span>
                        </div>
                    </label>
                    <div class="border-b border-gray-100"></div>
                    <label class="flex items-start">
                        <input type="checkbox" class="mt-1 mr-3 w-4 h-4 text-purple-600 rounded focus:ring-purple-500">
                        <div>
                            <span class="block font-bold text-sm text-gray-800">倫敦塔 & HMS Belfast 軍艦門票</span>
                            <span class="text-xs text-gray-500 block">官網線上購票不僅較便宜，還能省去現場排隊時間</span>
                            <span class="text-xs text-red-500 font-bold mt-1 bg-red-50 px-1 py-0.5 rounded inline-block">建議預約日: 出發前 1~2 週</span>
                        </div>
                    </label>
                </div>
            </div>
            """
            
            html_content = html_content[:block_start] + new_html_block + html_content[next_block:]
            print("Successfully updated HTML.")
        else:
            print("Could not find next block in HTML.")
    else:
        print("Could not find block start in HTML.")
else:
    print("Could not find tab-checklist in HTML.")

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Checklist updated.")
