import urllib.request
import re

queries = [
    "Tower Bridge walking tour london",
    "Buckingham Palace Changing of the Guard",
    "Natural History Museum London dinosaurs",
    "British Museum highlights",
    "Borough Market food tour london",
    "Cambridge Punting tour",
    "Sky Garden London view"
]

for q in queries:
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            print(f"{q}: {video_ids[0]}")
        else:
            print(f"{q}: Not found")
    except Exception as e:
        print(e)
