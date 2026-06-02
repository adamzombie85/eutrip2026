with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

def convert_accordions(html_content):
    search_str = '<div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">'
    
    parts = []
    current_pos = 0
    
    day_count = 1
    
    while True:
        start_idx = html_content.find(search_str, current_pos)
        if start_idx == -1:
            parts.append(html_content[current_pos:])
            break
            
        parts.append(html_content[current_pos:start_idx])
        
        # We found an opening div. Find the matching closing div.
        stack = 0
        i = start_idx
        closing_idx = -1
        
        while i < len(html_content):
            if html_content[i:i+4] == '<div':
                stack += 1
            elif html_content[i:i+6] == '</div':
                stack -= 1
                if stack == 0:
                    closing_idx = i
                    break
            i += 1
            
        if closing_idx == -1:
            # Should not happen if HTML is well-formed
            parts.append(html_content[start_idx:])
            break
            
        # Extract the day block content
        day_block = html_content[start_idx + len(search_str):closing_idx]
        
        # Transform the block
        # 1. Opening div -> details
        open_attr = ' open' if day_count == 1 else ''
        transformed = f'<details class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group"{open_attr}>'
        
        # 2. button -> summary
        import re
        day_block = re.sub(
            r'<button @click="activeDay = activeDay === \d+ \? null : \d+" class="w-full flex justify-between items-center p-4 focus:outline-none">',
            r'<summary class="w-full flex justify-between items-center p-4 focus:outline-none cursor-pointer list-none">',
            day_block
        )
        
        # 3. closing button -> closing summary
        # Also replace the chevron icon
        day_block = re.sub(
            r'<i style="display:none" class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300" :class="activeDay === \d+ \? \'rotate-180\' : \'\'"></i>\s*</button>',
            r'<span class="text-gray-400 transition-transform duration-300 group-open:rotate-180 text-xl">🔽</span>\n                    </summary>',
            day_block
        )
        
        # 4. opening div of content x-show -> div
        day_block = re.sub(
            r'<div x-show="activeDay === \d+" x-collapse>',
            r'<div>',
            day_block
        )
        
        transformed += day_block
        transformed += '</details>'
        
        parts.append(transformed)
        current_pos = closing_idx + 6 # skip </div>
        day_count += 1
        
    return ''.join(parts)

new_html = convert_accordions(html)

with open('London_Trip_Map.html', 'w') as f:
    f.write(new_html)

