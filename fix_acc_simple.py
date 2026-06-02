import re

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

for i in range(1, 9):
    # The start of the block
    old_start = f'<div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">\n                    <button @click="activeDay = activeDay === {i} ? null : {i}" class="w-full flex justify-between items-center p-4 focus:outline-none">'
    open_attr = ' open' if i == 1 else ''
    new_start = f'<details class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group"{open_attr}>\n                    <summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">'
    html = html.replace(old_start, new_start)

    # The button closing and chevron
    old_chevron = f'<i style="display:none" class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300" :class="activeDay === {i} ? \'rotate-180\' : \'\'"></i>\n                    </button>'
    new_chevron = '<span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>\n                    </summary>'
    html = html.replace(old_chevron, new_chevron)

    # The content opening
    old_content_open = f'<div x-show="activeDay === {i}" x-collapse>'
    new_content_open = f'<div>'
    html = html.replace(old_content_open, new_content_open)

# The tricky part: closing </details>.
# We can find all instances of '</div>\n\n                <!-- Day' and replace with '</details>\n\n                <!-- Day'
html = re.sub(r'</div>\n\n                <!-- Day', r'</details>\n\n                <!-- Day', html)

# For the last one (Day 8), it's followed by </div>\n        </div>
# Let's find Day 8's start and find its corresponding closing div.
html = html.replace('</div>\n\n            </div>\n        </div>\n\n        <!-- Tab: 必備清單', '</details>\n\n            </div>\n        </div>\n\n        <!-- Tab: 必備清單')


with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
