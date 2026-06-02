import re

with open('index.html', 'r') as f:
    html = f.read()

replacements = {
    '西敏寺與大笨鐘+London': 'Westminster+Abbey+London',
    '衛兵交接+(The+Mall)+London': 'Changing+of+the+Guard+The+Mall+London',
    '聖詹姆士公園野餐+London': 'St+James+Park+London',
    '聖凱瑟琳碼頭+London': 'St+Katharine+Docks+London',
    '自然史博物館+(需預約)+London': 'Natural+History+Museum+London',
    '科學博物館+&+Wonderlab+London': 'Science+Museum+London',
    'Harrods+貴婦百貨+London': 'Harrods+London',
    '海德公園+London': 'Hyde+Park+London',
    '大英博物館+(免費，需預約)+London': 'British+Museum+London',
    '柯芬園+&+Neil\'s+Yard+London': 'Covent+Garden+London',
    'Flat+Iron+牛排+London': 'Flat+Iron+London',
    'M&M\'s+與樂高樂園+London': 'M&M+World+London',
    '波羅市場+Borough+Market+London': 'Borough+Market+London',
    '泰特現代藝術館+(Tate+Modern)+London': 'Tate+Modern+London',
    '千禧橋與聖保羅大教堂+London': 'Millennium+Bridge+London',
    '南岸+Pizza+Express+London': 'Pizza+Express+Southbank+London',
    '南岸女王步道+London': 'The+Queens+Walk+London',
    '光影噴泉+London': 'Granary+Square+Fountains+London',
    '室內森林+London': 'Crossrail+Place+Roof+Garden+London',
    '倫敦塔+(付費門票)+London': 'Tower+of+London',
    '倫敦塔週邊+Wagamama+London': 'Wagamama+Tower+Hill+London',
    '倫敦塔橋+(Tower+Bridge)+London': 'Tower+Bridge+London',
    '+(Sainsbury\'s)+London': 'Sainsburys+London',
    'Pret+A+Manger+輕食+London': 'Pret+A+Manger+London',
    '國王學院': 'Kings+College',
    '與食屍鬼鐘': 'Corpus+Clock',
    '康河撐篙+(Punting)+Cambridge+UK': 'Scudamores+Punting+Cambridge+UK',
    '劍橋市集與午餐+Cambridge+UK': 'Cambridge+Market+Square+UK',
    '學院巡禮與買特產+London': 'Cambridge+University+UK',
    'Pizza+Union+King\'s+Cross': 'Pizza+Union+Kings+Cross+London',
    'Canary+Wharf+Franco+Manca+披薩+London': 'Franco+Manca+Canary+Wharf+London',
    '機場+Premier+Inn+餐廳+London': 'Premier+Inn+London+Heathrow+Airport',
}

for old, new in replacements.items():
    html = html.replace(f'https://www.google.com/maps/search/{old}', f'https://www.google.com/maps/search/{new}')

# special case for King's College which had tags embedded but I cleaned them up, wait I didn't clean them up in the previous script!
# Oh, King's College was: 國王學院 <span ...> 與食屍鬼鐘 <span ...>+Cambridge+UK
# Let's fix that one exactly.

html = re.sub(
    r'href="https://www.google.com/maps/search/國王學院[^"]+Cambridge\+UK"', 
    'href="https://www.google.com/maps/search/Kings+College+and+Corpus+Clock+Cambridge+UK"', 
    html
)

with open('index.html', 'w') as f:
    f.write(html)
