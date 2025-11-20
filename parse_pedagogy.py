import requests
from bs4 import BeautifulSoup
import json

URL = 'https://pedsovet.org/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div', class_='cards-unt-item')
articles = []

for card in cards:
    title_block = card.find('div', class_='cards-unt-item__title')
    if title_block:
        link = title_block.find('a')
        if link:
            title_text = link.get_text(strip=True)
            href = link.get('href')
            
            if href.startswith('/'):
                href = 'https://pedsovet.org' + href
            
            articles.append({
                'title': title_text,
                'link': href
            })

# Простой вывод
print("Найдено статей:", len(articles))
print()

for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(article['link'])
    print()

# Сохраняем в JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)