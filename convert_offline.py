import re

with open('tailwind_compiled.css', 'r') as f:
    tailwind_css = f.read()

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

# 1. Replace Tailwind CDN with compiled CSS and add custom CSS for tabs
css_injection = f"""
    <!-- Offline Tailwind CSS & CSS Tabs -->
    <style>
    {tailwind_css}
    
    /* CSS-only tabs */
    #tab-itinerary, #tab-videos, #tab-checklist {{ display: none !important; }}
    #radio-itinerary:checked ~ .mobile-app #tab-itinerary {{ display: block !important; }}
    #radio-videos:checked ~ .mobile-app #tab-videos {{ display: block !important; }}
    #radio-checklist:checked ~ .mobile-app #tab-checklist {{ display: block !important; }}

    #radio-itinerary:checked ~ .bottom-nav label[for="radio-itinerary"] {{ color: #2563eb !important; }}
    #radio-videos:checked ~ .bottom-nav label[for="radio-videos"] {{ color: #2563eb !important; }}
    #radio-checklist:checked ~ .bottom-nav label[for="radio-checklist"] {{ color: #2563eb !important; }}
    
    /* Hide scrollbar for details */
    summary::-webkit-details-marker {{ display: none; }}
    summary {{ list-style: none; }}
    </style>
    <!-- FontAwesome CSS (Better offline fallback than JS) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""
html = re.sub(r'<script src="https://cdn.tailwindcss.com"></script>', css_injection, html)
html = re.sub(r'<script src="https://kit.fontawesome.com/[a-zA-Z0-9]+.js"[^>]*></script>', '', html)
html = re.sub(r'<script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/collapse.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script defer src="https://cdn.jsdelivr.net/npm/alpinejs.*?</script>', '', html, flags=re.DOTALL)

# 2. Add Radio buttons after body
radios = """
<body>
<input type="radio" name="tabs" id="radio-itinerary" class="hidden" checked>
<input type="radio" name="tabs" id="radio-videos" class="hidden">
<input type="radio" name="tabs" id="radio-checklist" class="hidden">
"""
html = html.replace('<body>', radios)

# 3. Replace Bottom Navigation buttons with labels
html = re.sub(r'<div class="fixed bottom-0.*?>', lambda m: m.group(0).replace('fixed bottom-0', 'fixed bottom-0 bottom-nav'), html)

html = re.sub(r'<button onclick="switchTab\(\'itinerary\'\)".*?>\s*<i (.*?)></i>\s*<span (.*?)>每日行程</span>\s*</button>', 
              r'<label for="radio-itinerary" class="tab-btn flex flex-col items-center justify-center w-full h-full transition-colors relative text-gray-400 cursor-pointer"><i \1></i><span \2>每日行程</span></label>', html, flags=re.DOTALL)

html = re.sub(r'<button onclick="switchTab\(\'videos\'\)".*?>\s*<i (.*?)></i>\s*<span (.*?)>行前神遊</span>\s*</button>', 
              r'<label for="radio-videos" class="tab-btn flex flex-col items-center justify-center w-full h-full transition-colors relative text-gray-400 cursor-pointer"><i \1></i><span \2>行前神遊</span></label>', html, flags=re.DOTALL)

html = re.sub(r'<button onclick="switchTab\(\'checklist\'\)".*?>\s*<i (.*?)></i>\s*<span (.*?)>預約與採買</span>\s*</button>', 
              r'<label for="radio-checklist" class="tab-btn flex flex-col items-center justify-center w-full h-full transition-colors relative text-gray-400 cursor-pointer"><i \1></i><span \2>預約與採買</span></label>', html, flags=re.DOTALL)

# Remove the JS tab script
html = re.sub(r'<script>\s*function switchTab\(tab\).*?</script>', '', html, flags=re.DOTALL)

# 4. Replace Accordions with <details> and <summary>
def repl_accordion(m):
    day_num = m.group(1)
    title = m.group(2)
    content = m.group(3)
    
    # Is it Day 1? Make it open by default
    open_attr = "open" if "Day 1" in day_num else ""
    
    return f"""<details class="mb-4 bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group" {open_attr}>
    <summary class="p-4 cursor-pointer flex justify-between items-center bg-gray-50 border-b border-gray-100 list-none">
        <div>
            {day_num}
            {title}
        </div>
        <i class="fa-solid fa-chevron-down text-gray-600 group-open:rotate-180 transition-transform duration-300"></i>
    </summary>
    <div class="p-4 text-gray-700 space-y-4">
        {content}
    </div>
</details>"""

# Match Alpine accordions
pattern = r'<div class="mb-4 bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden" x-data="\{ expanded: (?:true|false) \}">\s*<!-- Day Header -->\s*<div @click="expanded = !expanded" class="p-4 cursor-pointer flex justify-between items-center bg-gray-50 border-b border-gray-100">\s*<div>\s*(.*?)\s*(<h2.*?>.*?</h2>)\s*</div>\s*<i.*?</i>\s*</div>\s*<!-- Itinerary Content -->\s*<div x-show="expanded" x-collapse>\s*<div class="p-4 text-gray-700 space-y-4">\s*(.*?)\s*</div>\s*</div>\s*</div>'

html = re.sub(pattern, repl_accordion, html, flags=re.DOTALL)

# 5. Fix YouTube IDs
youtube_map = {
    "5U9-YJnt37s": "EvSkDqUNJGU", # Tower Bridge
    "5U9-YJnt37s": "cM70wwHKWMM", # Buckingham (wait I reused fake IDs?)
    "sZ5i8C5pIqQ": "qkNNljDOyeg", # Natural history
    "m6169KkRjI8": "aZv6i01De2Q", # British museum
    "U3lWf0B-7eU": "w3TuFQyaOTA", # Borough
    "zR7-eH0Qn4I": "jftLVTpBpJw", # Cambridge
    "yVqX-g_H7O4": "QrLIuv4w1pU"  # Sky Garden
}

# In the original HTML, Day 1 had 5U9-YJnt37s, Day 2 had 5U9-YJnt37s! Let's just use string replace carefully
html = html.replace('Day 1: 倫敦塔橋 (Tower Bridge)</h3>\\n                    <div class="aspect-w-16 aspect-h-9 relative" style="padding-bottom: 56.25%;">\\n                        <iframe class="absolute top-0 left-0 w-full h-full rounded-lg" src="https://www.youtube.com/embed/5U9-YJnt37s"',
                    'Day 1: 倫敦塔橋 (Tower Bridge)</h3>\\n                    <div class="aspect-w-16 aspect-h-9 relative" style="padding-bottom: 56.25%;">\\n                        <iframe class="absolute top-0 left-0 w-full h-full rounded-lg" src="https://www.youtube.com/embed/EvSkDqUNJGU"')

html = html.replace('Day 2: 白金漢宮衛兵交接</h3>\\n                    <div class="aspect-w-16 aspect-h-9 relative" style="padding-bottom: 56.25%;">\\n                        <iframe class="absolute top-0 left-0 w-full h-full rounded-lg" src="https://www.youtube.com/embed/5U9-YJnt37s"',
                    'Day 2: 白金漢宮衛兵交接</h3>\\n                    <div class="aspect-w-16 aspect-h-9 relative" style="padding-bottom: 56.25%;">\\n                        <iframe class="absolute top-0 left-0 w-full h-full rounded-lg" src="https://www.youtube.com/embed/cM70wwHKWMM"')

for old_id, new_id in youtube_map.items():
    html = html.replace(f'embed/{old_id}', f'embed/{new_id}')

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)

print("Conversion complete!")
