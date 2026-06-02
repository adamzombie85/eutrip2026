import re

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

# Replace bottom tabs
html = html.replace('<i class="fa-solid fa-map-location-dot text-xl mb-1 pointer-events-none"></i>', '<span class="text-xl mb-1 pointer-events-none">📍</span>')
html = html.replace('<i class="fa-brands fa-youtube text-xl mb-1 pointer-events-none"></i>', '<span class="text-xl mb-1 pointer-events-none">📺</span>')
html = html.replace('<i class="fa-solid fa-list-check text-xl mb-1 pointer-events-none"></i>', '<span class="text-xl mb-1 pointer-events-none">✅</span>')

# Replace other icons
html = html.replace('<i class="fa-solid fa-house-chimney mr-3 text-xl"></i>', '<span class="mr-3 text-xl">🏠</span>')
html = html.replace('<i class="fa-solid fa-location-arrow mr-2"></i>', '<span class="mr-2">🧭</span>')
html = html.replace('<i class="fa-regular fa-calendar mr-2"></i>', '<span class="mr-2">📅</span>')
html = html.replace('<i class="fa-solid fa-train-subway mr-1"></i>', '<span class="mr-1">🚇</span>')
html = html.replace('<i class="fa-solid fa-location-dot text-blue-500 text-[12px] ml-0.5"></i>', '<span class="ml-0.5 text-[12px]">📍</span>')
html = html.replace('<i class="fa-solid fa-play text-blue-400 text-[10px] mr-1"></i>', '<span class="mr-1 text-[10px]">▶️</span>')
html = html.replace('<i class="fa-solid fa-chevron-down', '<i style="display:none" class="fa-solid fa-chevron-down') # Hide any remaining chevrons since native details has an arrow

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
