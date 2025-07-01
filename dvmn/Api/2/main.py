import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


load_dotenv()
token = os.getenv("VK_API_TOKEN")
    

def is_shorten_link(url):
    parsed = urlparse(url)
    return parsed.netloc == "vk.cc"


def count_clicks(token, short_link):
    try:
        key = short_link.split('/')[-1]
    except IndexError:
        return "Некорректный формат сокращенной ссылки"
    
    url = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        "access_token":token,
        "key": key,
        "v": "5.131",
        "source": "vk_cc",
        "interval": "forever",
        "extended": 0
        }
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        json_data = response.json()
        views = json_data['response']['stats']
        return views[0]['views']
    except (KeyError, IndexError, TypeError) as e:
        return f"Ошибка обработки данных: {e}"


def shorten_link(token, original_url):
    url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        "access_token":token,
        "v": "5.131",
        "url": original_url
        }
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        return response.json()['response']['short_url']
    except KeyError:
        return "Ошибка при сокращении ссылки"

if __name__ == "__main__":
    user_input = input("Введите ссылку: ").strip()
    if is_shorten_link(user_input):
        print("Проверка статистики...")
        clicks = count_clicks(token, user_input)
        print(f"Количество кликов: {clicks}")
    else:
        print("Сокращение ссылки...")
        short_url = shorten_link(token, user_input)
        print(f"Сокращенная ссылка: {short_url}")



