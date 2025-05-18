import os
import json
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

HTML_FILE = 'paste.txt'
SAVE_DIR = 'webp_images'
HEROES_JSON = 'data/heroes.json'

os.makedirs(SAVE_DIR, exist_ok=True)

# Загрузить JSON с id и именами героев
with open(HEROES_JSON, encoding='utf-8') as f:
    heroes = json.load(f)  # словарь вида {"128": "Kalea", ...}

# Создать обратный словарь name -> id для быстрого поиска
name_to_id = {v: k for k, v in heroes.items()}

# Загрузить HTML
with open(HTML_FILE, encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Найти все img теги
img_tags = soup.find_all('img')

# Найти все div с классом mt-text, где содержится имя героя
divs = soup.find_all('div', class_='mt-text')

# Сопоставить имена героев из div с url картинок по src или data-src
# Предполагаем, что img и div идут в одном порядке или есть способ сопоставить
# Если нет, можно расширить логику под ваши данные.

# Собираем имена героев из div
hero_names_in_html = []
for div in divs:
    span = div.find('span')
    if span:
        hero_names_in_html.append(span.text.strip())

# Собираем url изображений
urls = []
for tag in img_tags:
    url = tag.get('src') or tag.get('data-src')
    if url and url.startswith('http'):
        urls.append(url)

print(f'Найдено изображений: {len(urls)}')
print(f'Найдено героев в HTML: {len(hero_names_in_html)}')

# Предположим, что количество героев и изображений совпадает и порядок тоже
# Если нет, нужно уточнить логику сопоставления
for hero_name, url in zip(hero_names_in_html, urls):
    hero_id = name_to_id.get(hero_name)
    if not hero_id:
        print(f'Не найден id для героя с именем {hero_name}, пропускаем')
        continue
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert('RGBA')
        webp_path = os.path.join(SAVE_DIR, f'{hero_id}.webp')
        img.save(webp_path, 'webp')
        print(f'Сохранено: {webp_path} (герой: {hero_name})')
    except Exception as e:
        print(f'Ошибка с {url} для героя {hero_name}: {e}')
