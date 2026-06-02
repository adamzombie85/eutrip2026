import re

with open('index.html', 'r') as f:
    html = f.read()

def clean_href(match):
    href = match.group(0)
    # Remove spans
    cleaned = re.sub(r'<span[^>]*>.*?</span>', '', href)
    # Remove leading/trailing spaces before +London or within the query if it broke
    # E.g. "西敏寺與大笨鐘 +London" -> "西敏寺與大笨鐘+London"
    cleaned = cleaned.replace(' +London', '+London')
    return cleaned

new_html = re.sub(r'href="[^"]+"', clean_href, html)

with open('index.html', 'w') as f:
    f.write(new_html)
