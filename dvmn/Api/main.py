import requests


def get_weather(town):
    payload = {"nTqM": "", "lang": "ru"}
    url_with_town = f'https://wttr.in/{town}'
    response = requests.get(url_with_town, params=payload)
    response.raise_for_status()
    return response.text


def main():
    town_weather = get_weather("Череповец")
    print(town_weather)


if __name__ == "__main__":
    main()