with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

html = html.replace('<details class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group"', '<details name="itinerary-days" class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group"')

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
