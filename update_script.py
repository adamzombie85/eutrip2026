import re

md_content = """# 🇬🇧 倫敦 9 天 8 夜家庭窮遊計畫 (專屬客製化 V2 版)

**住宿地點**：Whitechapel / Nelson St

## 📌 住宿點優勢分析
*   **地點**：Nelson Street, E1 (靠近 Whitechapel 站)。
*   **交通**：Elizabeth Line (紫線) / District Line (綠線)。
*   **生活**：步行 5-10 分鐘有大型 Sainsbury's 和 Tesco，是省錢自炊的黃金地帶。
*   **周邊隱藏版 (適合你們)**：走路就能到 **Spitalfields City Farm (城市農場)** 與 **Old Spitalfields Market (老斯皮塔佛德市集)**，完美結合小孩愛動物與媽媽愛逛街吃美食的需求！

---

## 🗓️ 每日行程規劃 (依據家庭喜好調整)

### Day 1 (7/23): 抵達與泰晤士河初探
*   **行程點 1：Airbnb 放置行李與周邊熟悉**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：熟悉 Whitechapel 車站周邊動線與超市位置。
*   **行程點 2：倫敦塔橋 (Tower Bridge) 看夜景**
    *   **建議停留時間**：1.5 小時
    *   **必逛看點**：漫步橋上拍泰晤士河延伸感，從女王步道拍塔橋全景。媽媽絕佳拍照點，爸爸的歷史建築起點。
*   **行程點 3：Sainsbury's 超市採買晚餐**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：搶購黃標烤雞、義大利麵等。爸爸可挑選綜合生菜沙拉補充纖維質。

### Day 2 (7/24): 西敏寺經典地標 & 皇家動物生態
*   **行程點 1：大笨鐘與西敏寺 (外觀)**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：走到西敏橋上拍大笨鐘與紅色雙層巴士同框照。爸爸可藉機欣賞西敏寺哥德式建築歷史。
*   **行程點 2：聖詹姆士公園 (St James's Park)**
    *   **建議停留時間**：1.5 小時 (含野餐)
    *   **必逛看點**：公園內有超多不怕人的松鼠、天鵝與大鵜鶘 (Pelican)！小孩絕對會愛死，適合讓小孩嘗試用英文問路人動物名字，中午在此享用 Meal Deal。
*   **行程點 3：白金漢宮衛兵交接**
    *   **建議停留時間**：1.5 小時
    *   **必逛看點**：在林蔭大道 (The Mall) 或威靈頓軍營觀看交接儀式，避開正門人擠人，媽媽必拍的英倫風情。

### Day 3 (7/25): 南肯辛頓博物館區 (小孩放電 + 媽媽血拚)
*   **行程點 1：自然史博物館**
    *   **建議停留時間**：2.5 小時
    *   **必逛看點**：直奔恐龍區 (Dinosaurs) 看會動的 T-Rex 模型，再去大廳看巨大藍鯨骨架 (Hope)，並搭乘穿透金屬球的「地球內部」電扶梯。
*   **行程點 2：科學博物館 (含 Wonderlab)**
    *   **建議停留時間**：3 小時
    *   **必逛看點**：館內有大量「互動式操作機台」。若有 Wonderlab 門票，必玩摩擦力溜滑梯與觀看定時化學秀，小孩絕對放電完畢。
*   **行程點 3：Harrods 貴婦百貨**
    *   **建議停留時間**：2 小時
    *   **必逛看點**：媽媽享受奢華建築拍照與逛街。傍晚至地下一樓食品區搶特價的高級熟食做為晚餐。

### Day 4 (7/26): 文明瑰寶與街頭藝術
*   **行程點 1：大英博物館**
    *   **建議停留時間**：3.5 小時
    *   **必逛看點**：爸爸用 Gemini APP 擔任說書人！帶著小孩尋找：羅塞塔石碑、木乃伊、復活節島摩艾石像。把逛古蹟變成尋寶遊戲。
*   **行程點 2：牛津街 (Oxford Street)**
    *   **建議停留時間**：1.5 小時
    *   **必逛看點**：媽媽的購物天堂，平價服飾與紀念品店林立。
*   **行程點 3：柯芬園 (Covent Garden)**
    *   **建議停留時間**：2.5 小時
    *   **必逛看點**：極具水準的街頭藝人表演 (魔術、雜耍)，小孩看得開心，媽媽可逛蘋果市集。小孩可在周邊攤販練習用英文點餐小吃。

### Day 5 (7/27): 南岸美食與「真軍艦」探險
*   **行程點 1：Borough Market (波羅市場)**
    *   **建議停留時間**：2 小時
    *   **必逛看點**：倫敦最著名的美食市集！媽媽可品嚐各國特色料理 (如海鮮燉飯)，小孩沿路吃零食，爸爸尋找健康蔬食。
*   **行程點 2：HMS Belfast (貝爾法斯特號軍艦)**
    *   **建議停留時間**：2.5 小時
    *   **必逛看點**：停在泰晤士河上的真實二戰巡洋艦！小孩可在艦橋、船艙裡爬上爬下操作機關；爸爸看海軍歷史；媽媽在甲板上拍塔橋無敵美景。
*   **行程點 3：千禧橋與南岸漫步**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：走過哈利波特電影中的千禧橋，遠眺聖保羅大教堂圓頂。

### Day 6 (7/28): 劍橋 (Cambridge) 大學城一日遊
*   **行程點 1：劍橋國王學院與校園漫步**
    *   **建議停留時間**：2 小時
    *   **必逛看點**：欣賞哥德式建築之美 (爸爸歷史點)，尋找徐志摩詩碑，校園極好拍照 (媽媽拍照點)。
*   **行程點 2：康河撐篙 (Punting)**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：互動性高，小孩會覺得像坐船探險，沿途穿梭嘆息橋與數學橋，享受英倫大學城悠閒氛圍。
*   **行程點 3：劍橋草地野餐**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：自備三明治，在劍橋大片綠地上野餐，讓小孩奔跑放風。

### Day 7 (7/29): 巨石陣與羅馬浴場 (Railcard 發威日)
*   **行程點 1：巨石陣 (Stonehenge)**
    *   **建議停留時間**：2 小時 (不含車程)
    *   **必逛看點**：史前遺跡的震撼！小孩可在廣大平原上走跳，沿途火車還能看到英國鄉間綿羊與牛群。爸爸沉浸於史前歷史。
*   **行程點 2：巴斯 (Bath) 羅馬浴場與市區**
    *   **建議停留時間**：3 小時
    *   **必逛看點**：爸爸必看古羅馬浴場遺跡。巴斯建築呈現蜜糖色，拍照極美 (媽媽愛死)。
*   **行程點 3：Sally Lunn's 圓麵包**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：品嚐巴斯著名的傳統下午茶點心，媽媽的美食清單必打卡。

### Day 8 (7/30): 倫敦塔與空中花園 (大餐) ➜ 機場
*   **行程點 1：倫敦塔 (Tower of London)**
    *   **建議停留時間**：2.5 小時
    *   **必逛看點**：爸爸必看的英國王室血腥歷史與超華麗「皇冠珠寶」。可聽 Beefeater (皇家衛兵) 導覽，用 Gemini 幫小孩即時翻譯故事。
*   **行程點 2：Sky Garden (空中花園) 景觀大餐**
    *   **建議停留時間**：2 小時
    *   **必逛看點**：在景觀餐廳吃豐盛告別大餐，俯瞰倫敦無敵市景！媽媽最期待的拍照與美食行程。(強烈建議提前上網訂位，訂位成功免搶免費票)。
*   **行程點 3：Spitalfields City Farm (視時間彈性)**
    *   **建議停留時間**：1 小時
    *   **必逛看點**：回住處拿行李前順路去免費城市農場，摸羊跟看小毛驢，完美收尾。

---

## 💡 針對家庭成員的專屬建議

1.  **爸爸的 AI 專武**：
    *   準備好 Gemini 的手機 APP。在**大英博物館**或**倫敦塔**時，可以隨時對著看不懂的英文解說牌拍照，讓 Gemini 即時翻譯並「用說故事的方式講給小孩聽」，會大幅增加小孩看古蹟的興趣。
2.  **媽媽的美食與拍照**：
    *   **Borough Market** 跟 **老斯皮塔佛德市集 (Old Spitalfields Market, 離住處很近)** 是你的天堂。
    *   在英國吃飯如果爸爸需要纖維質，可以隨時走進 **Pret A Manger** 或 **Leon**（英國到處都是的健康快餐連鎖），裡面有超多沙拉與熱蔬食餐盒。
3.  **小孩的英文互動**：
    *   在市集買小吃、在超市買東西結帳時，是最好的練習機會。教他們說：「*Can I have this one, please?*」和「*Thank you!*」，英國人通常對小孩非常友善，這會給他們很大的成就感。
"""

with open("UK_Trip_Itinerary_V2.md", "w", encoding="utf-8") as f:
    f.write(md_content)

days_html = """
                <!-- Day 1 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group" open>
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">1</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">抵達與泰晤士河初探</h3>
                                <p class="text-xs text-gray-500">7/23 (四) • 建議出門: 16:00</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Airbnb 放置行李與周邊熟悉</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>熟悉 Whitechapel 車站周邊動線與超市位置。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Tower+Bridge+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">倫敦塔橋 (Tower Bridge) 看夜景 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>漫步橋上拍泰晤士河延伸感，從女王步道拍塔橋全景。媽媽絕佳拍照點，爸爸的歷史建築起點。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Sainsbury's 超市採買晚餐</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>搶購黃標烤雞、義大利麵等。爸爸可挑選綜合生菜沙拉補充纖維質。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 2 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">2</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">西敏寺經典地標 & 皇家動物生態</h3>
                                <p class="text-xs text-gray-500">7/24 (五) • 建議出門: 08:30</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Westminster+Abbey+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">大笨鐘與西敏寺 (外觀) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>走到西敏橋上拍大笨鐘與紅色雙層巴士同框照。爸爸可藉機欣賞西敏寺哥德式建築歷史。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/St+James+Park+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">聖詹姆士公園 (St James's Park) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>公園內有超多不怕人的松鼠、天鵝與大鵜鶘 (Pelican)！小孩絕對會愛死，適合讓小孩嘗試用英文問路人動物名字，中午在此享用 Meal Deal。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Changing+of+the+Guard+The+Mall+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">白金漢宮衛兵交接 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>在林蔭大道 (The Mall) 或威靈頓軍營觀看交接儀式，避開正門人擠人，媽媽必拍的英倫風情。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 3 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">3</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">南肯辛頓博物館區</h3>
                                <p class="text-xs text-gray-500">7/25 (六) • 建議出門: 08:45</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Natural+History+Museum+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">自然史博物館 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>直奔恐龍區看會動的 T-Rex 模型，大廳看巨大藍鯨骨架 (Hope)，並搭乘穿透金屬球的「地球內部」電扶梯。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Science+Museum+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">科學博物館 (含 Wonderlab) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 3 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>館內有大量「互動式操作機台」。必玩摩擦力溜滑梯與觀看定時化學秀，小孩絕對放電完畢。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Harrods+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">Harrods 貴婦百貨 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>媽媽享受奢華建築拍照與逛街。傍晚至地下一樓食品區搶特價的高級熟食做為晚餐。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 4 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">4</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">文明瑰寶與街頭藝術</h3>
                                <p class="text-xs text-gray-500">7/26 (日) • 建議出門: 09:15</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/British+Museum+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">大英博物館 <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 3.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>爸爸用 Gemini APP 擔任說書人！帶著小孩尋找：羅塞塔石碑、木乃伊、復活節島摩艾石像，把逛古蹟變成尋寶遊戲。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Oxford+Street+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">牛津街 (Oxford Street) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>媽媽的購物天堂，平價服飾與紀念品店林立。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Covent+Garden+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">柯芬園 (Covent Garden) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>極具水準的街頭藝人表演，小孩看得開心，媽媽可逛蘋果市集。小孩可在周邊攤販練習用英文點餐小吃。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 5 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">5</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">南岸美食與「真軍艦」探險</h3>
                                <p class="text-xs text-gray-500">7/27 (一) • 建議出門: 10:00</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/Borough+Market+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">Borough Market (波羅市場) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>倫敦最著名的美食市集！媽媽可品嚐各國特色料理 (如海鮮燉飯)，小孩沿路吃零食，爸爸尋找健康蔬食。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm"><a href="https://www.google.com/maps/search/HMS+Belfast+London" target="_blank" class="hover:text-blue-600 transition-colors inline-flex items-center gap-1">HMS Belfast (貝爾法斯特號軍艦) <span class="ml-0.5 text-[12px]">📍</span></a></p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>停在泰晤士河上的真實二戰巡洋艦！小孩可在艦橋、船艙裡爬上爬下；爸爸看海軍歷史；媽媽在甲板上拍塔橋無敵美景。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">千禧橋與南岸漫步</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>走過哈利波特電影中的千禧橋，遠眺聖保羅大教堂圓頂。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 6 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">6</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">劍橋 (Cambridge) 一日遊</h3>
                                <p class="text-xs text-gray-500">7/28 (二) • 建議出門: 08:30</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">劍橋國王學院與校園漫步</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>欣賞哥德式建築之美 (爸爸歷史點)，尋找徐志摩詩碑，校園極好拍照 (媽媽拍照點)。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">康河撐篙 (Punting)</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>互動性高，小孩會覺得像坐船探險，沿途穿梭嘆息橋與數學橋，享受英倫大學城悠閒氛圍。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">劍橋草地野餐</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>自備三明治，在劍橋大片綠地上野餐，讓小孩奔跑放風。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 7 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">7</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">巨石陣與羅馬浴場</h3>
                                <p class="text-xs text-gray-500">7/29 (三) • 建議出門: 08:00</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">巨石陣 (Stonehenge)</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>史前遺跡的震撼！小孩可在廣大平原上走跳，沿途火車還能看到英國鄉間綿羊與牛群。爸爸沉浸於史前歷史。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">巴斯 (Bath) 羅馬浴場與市區</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 3 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>爸爸必看古羅馬浴場遺跡。巴斯建築呈現蜜糖色，拍照極美 (媽媽愛死)。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Sally Lunn's 圓麵包</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>品嚐巴斯著名的傳統下午茶點心，媽媽的美食清單必打卡。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>

                <!-- Day 8 -->
                <details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group">
                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">
                        <div class="flex items-center">
                            <div class="bg-blue-100 text-blue-600 font-bold rounded-lg w-12 h-12 flex flex-col justify-center items-center mr-4">
                                <span class="text-xs">Day</span>
                                <span class="text-lg leading-none">8</span>
                            </div>
                            <div class="text-left">
                                <h3 class="font-bold text-gray-800">倫敦塔與空中花園</h3>
                                <p class="text-xs text-gray-500">7/30 (四) • 建議出門: 09:00</p>
                            </div>
                        </div>
                        <span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>
                    </summary>
                    <div>
                        <div class="p-4 pt-0 border-t border-gray-50 bg-gray-50/50">
                            <ul class="relative border-l border-gray-200 ml-3 mt-3 space-y-4 pb-2">
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-cyan-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">倫敦塔 (Tower of London)</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2.5 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>爸爸必看的英國王室血腥歷史與超華麗「皇冠珠寶」。可聽 Beefeater 導覽，用 Gemini 幫小孩即時翻譯故事。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-blue-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Sky Garden (空中花園) 景觀大餐</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 2 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>在景觀餐廳吃豐盛告別大餐，俯瞰倫敦無敵市景！媽媽最期待的拍照與美食行程。(強烈建議提前上網訂位)。</p>
                                </li>
                                <li class="pl-6 relative">
                                    <div class="absolute w-3 h-3 bg-purple-500 rounded-full -left-[6.5px] top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <p class="font-bold text-sm">Spitalfields City Farm</p>
                                        <span class="text-[10px] bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full">停留: 1 小時</span>
                                    </div>
                                    <p class="text-xs text-gray-600 mt-1"><span class="mr-1 text-[10px]">▶️</span> <strong>活動：</strong>回住處拿行李前順路去免費城市農場，摸羊跟看小毛驢，完美收尾。</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </details>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find the existing <!-- Days List --> div
# It starts with <div class="space-y-3"> right after <!-- Days List -->
# and ends right before <!-- Tab: 預約與採買 --> or </div> closing that tab.
start_idx = content.find('<div class="space-y-3">', content.find('<!-- Days List -->'))
end_idx = content.find('</div>\n\n        <!-- Tab: 預約與採買 (Checklist) -->', start_idx)
if end_idx == -1:
    end_idx = content.find('</div>\n\n        <!-- Tab: 預約清單', start_idx)
if end_idx == -1:
    # Let's search for the closing div manually. We know it ends before the next tab which starts with <!-- Tab:
    next_tab_idx = content.find('<!-- Tab:', start_idx)
    if next_tab_idx != -1:
        # Go back to find the closing div of the space-y-3 container
        end_idx = content.rfind('</div>', start_idx, next_tab_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + '<div class="space-y-3">\n' + days_html + '\n            ' + content[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated index.html")
else:
    print("Could not find the bounds for replacement.")
    print("start_idx:", start_idx, "end_idx:", end_idx)

# Let's also update the Video section if possible. 
# In index.html, there's a video for Sky Garden on Day 7, and Borough market on Day 5.
# We will just replace "Day 7: 倫敦 Sky Garden" with "Day 8: 倫敦 Sky Garden"
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace('Day 7: 倫敦 Sky Garden (空中花園)', 'Day 8: 倫敦 Sky Garden (空中花園)')
content = content.replace('Day 5: 波羅市場 (Borough Market) 美食', 'Day 5: HMS Belfast 與 Borough Market')
content = content.replace('Day 7: 倫敦 Sky Garden', 'Day 8: 倫敦 Sky Garden')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
