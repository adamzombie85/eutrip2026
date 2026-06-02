with open('tailwind_compiled.css', 'r') as f:
    css = f.read()

with open('London_Trip_Map.html', 'r') as f:
    html = f.read()

html = html.replace("<style>\\n    \\n    \\n    /* CSS-only tabs */", f"<style>\\n{css}\\n    /* CSS-only tabs */")

with open('London_Trip_Map.html', 'w') as f:
    f.write(html)
