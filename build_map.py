import urllib.request
import urllib.parse
import json
import time

locations = [
    ("Tower Bridge", "London Tower Bridge"),
    ("Sainsbury's", "Sainsbury's Whitechapel London"),
    ("Leadenhall Market", "Leadenhall Market London"),
    ("Westminster Abbey", "Westminster Abbey London"),
    ("The Mall (衛兵交接)", "The Mall London"),
    ("St James Park", "St James's Park London"),
    ("St Katharine Docks", "St Katharine Docks London"),
    ("Natural History Museum", "Natural History Museum London"),
    ("Science Museum", "Science Museum London"),
    ("Harrods", "Harrods London"),
    ("Hyde Park", "Hyde Park London"),
    ("British Museum", "British Museum London"),
    ("Pret A Manger", "Pret A Manger London"),
    ("Covent Garden", "Covent Garden London"),
    ("Flat Iron", "Flat Iron London"),
    ("M&M's World", "M&M World London"),
    ("Borough Market", "Borough Market London"),
    ("Tate Modern", "Tate Modern London"),
    ("Millennium Bridge", "Millennium Bridge London"),
    ("Pizza Express Southbank", "Pizza Express Southbank London"),
    ("The Queens Walk", "The Queens Walk London"),
    ("King's College Cambridge", "Kings College Cambridge UK"),
    ("Cambridge Market Square", "Cambridge Market Square UK"),
    ("Pizza Union King's Cross", "Pizza Union Kings Cross London"),
    ("Granary Square", "Granary Square London"),
    ("Sky Garden", "Sky Garden London"),
    ("Darwin Brasserie", "Darwin Brasserie London"),
    ("Museum of London Docklands", "Museum of London Docklands"),
    ("Franco Manca Canary Wharf", "Franco Manca Canary Wharf London"),
    ("Crossrail Place Roof Garden", "Crossrail Place Roof Garden London"),
    ("Tower of London", "Tower of London"),
    ("Wagamama Tower Hill", "Wagamama Tower Hill London"),
]

def geocode(query):
    url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query)}&format=json&limit=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'london_trip_planner_2026/1.0 (nelly@example.com)'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"Error querying {query}: {e}")
    return None

markers = []
for name, query in locations:
    time.sleep(1) # Be nice to nominatim
    loc = geocode(query)
    if loc:
        markers.append({"name": name, "lat": loc[0], "lon": loc[1]})
        print(f"Found {name}: {loc[0]}, {loc[1]}")
    else:
        # Fallback to name
        loc2 = geocode(name)
        if loc2:
            markers.append({"name": name, "lat": loc2[0], "lon": loc2[1]})
            print(f"Found fallback {name}: {loc2[0]}, {loc2[1]}")
        else:
            print(f"Could not find {name}")

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>倫敦親子遊 2026 - 行程地圖</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        #map {{ height: calc(100vh - 64px); width: 100%; }}
    </style>
</head>
<body class="bg-gray-100 m-0 p-0 font-sans">
    <div class="h-16 bg-blue-600 text-white flex items-center px-4 shadow-md">
        <h1 class="text-xl font-bold">🗺️ 倫敦親子遊 2026 - 景點地圖</h1>
        <a href="index.html" class="ml-auto bg-white text-blue-600 px-4 py-2 rounded-lg font-bold hover:bg-gray-100 text-sm">返回行程表</a>
    </div>
    <div id="map"></div>

    <script>
        var map = L.map('map').setView([51.5074, -0.1278], 12);

        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '&copy; OpenStreetMap contributors'
        }}).addTo(map);

        var locations = {json.dumps(markers)};
        
        var bounds = [];
        locations.forEach(function(loc) {{
            var marker = L.marker([loc.lat, loc.lon]).addTo(map);
            marker.bindPopup("<b>" + loc.name + "</b>");
            bounds.push([loc.lat, loc.lon]);
        }});

        if (bounds.length > 0) {{
            map.fitBounds(bounds);
        }}
    </script>
</body>
</html>"""

with open("London_Trip_Map.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Map generated: London_Trip_Map.html")
