import requests

url = 'https://wttr.in/london?nTqu'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Cherepovets?nTqu'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Череповец?nTqM&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)