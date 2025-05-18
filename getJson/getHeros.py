import requests
import json

def fetch_heroes():
    api_url = "https://api-mobilelegends.vercel.app/api/hero-list/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching heroes: {e}")
        return None

heroes_data = fetch_heroes()
if heroes_data is not None:
    with open('../data/heroes.json', 'w', encoding='utf-8') as f:
        json.dump(heroes_data, f, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в heroes.json")
else:
    print("Не удалось получить данные героев")