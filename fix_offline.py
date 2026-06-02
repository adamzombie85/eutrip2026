import re

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

# 1. Remove YouTube tab related stuff
# Remove radio button
html = re.sub(r'<input type="radio" name="tabs" id="radio-videos" class="hidden">\n?', '', html)
# Remove bottom nav label
html = re.sub(r'<label for="radio-videos".*?</label>\n?', '', html, flags=re.DOTALL)
# Remove custom CSS for videos
html = re.sub(r'#radio-videos:checked.*?}\n?', '', html)
html = re.sub(r'#tab-videos { display: none !important; }', '', html)
# Remove the tab content
html = re.sub(r'<div id="tab-videos" style="display: none;">.*?(?=<div id="tab-checklist")', '', html, flags=re.DOTALL)

# Also remove #tab-videos from CSS-only tabs
html = html.replace('#tab-itinerary, #tab-videos, #tab-checklist { display: none !important; }', '#tab-itinerary, #tab-checklist { display: none !important; }')

# 2. Remove external CDN scripts and links
html = html.replace('<script src="https://cdn.tailwindcss.com"></script>', '')
html = re.sub(r'<!-- FontAwesome CSS.*?<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">', '', html, flags=re.DOTALL)

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
