import os
import requests
import sys
from dotenv import load_dotenv
from urllib.parse import urlparse
    

def is_shorten_link(token, url):
    key = url.split('/')[-1]
    response = requests.get(
        'https://api.vk.com/method/utils.getLinkStats',
        params={
            "access_token": token,
            "key": key,
            "v": "5.131",
            "test_mode": 1
        }
    )
    response.raise_for_status()
    return 'response' in response.json()


def count_clicks(token, short_link):
    key = short_link.split('/')[-1]
    url = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        "access_token":token,
        "key": key,
        "v": "5.131",
        "source": "vk_cc",
        "interval": "forever",
        "extended": 0
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_data = response.json()
    views = response_data['response']['stats']
    return views[0]['views']


def shorten_link(token, original_url):
    url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        "access_token":token,
        "v": "5.131",
        "url": original_url
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']['short_url']


def main():
    load_dotenv()
    try:
        token = os.environ["VK_API_TOKEN"]
    except KeyError:
        sys.exit("Ошибка: VK_API_TOKEN не найден в переменных окружения")
    user_input = input("Введите ссылку: ").strip()
    try:
        if is_shorten_link(token, user_input):
            print("Проверка статистики...")
            clicks = count_clicks(token, user_input)
            print(f"Количество кликов: {clicks}")
        else:
            print("Сокращение ссылки...")
            short_url = shorten_link(token, user_input)
            print(f"Сокращенная ссылка: {short_url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ошибка: {e}")
    except IndexError as e:
        print(f"Некорректный формат ссылки: {e}")
    except KeyError as e:
        print(f"Ошибка в структуре API-ответа: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()