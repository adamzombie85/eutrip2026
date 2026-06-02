with open('tailwind_compiled.css', 'r') as f:
    css = f.read()

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

injection = f"<style>\n{css}\n</style>"
html = html.replace('<title>倫敦親子窮遊 2026</title>', f"<title>倫敦親子窮遊 2026</title>\n{injection}")

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
