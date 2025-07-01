import json
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from geopy import distance
import folium


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return float(lat), float(lon)


def get_distance(coffee_shop):
    return coffee_shop["distance"]


def main():
    load_dotenv()
    apikey = os.getenv('YANDEX_API_KEY')
    user_address = input("Где вы находитесь? ")
    user_coords = fetch_coordinates(apikey, user_address)
    base_path = Path(__file__).absolute().parent
    file_path = base_path / 'coffee.json'
    with open(file_path, 'r', encoding='windows-1251') as file:
        data = json.load(file)
        coffee_shops = []
        for item in data:
            name_value = item.get("Name")
            latitude_value = item.get("Latitude_WGS84")
            longitude_value = item.get("Longitude_WGS84")
            coffee_coords_geopy = (float(latitude_value), float(longitude_value))
            dist_to_user = distance.distance(coffee_coords_geopy, user_coords).km
            coffee_shops.append({
                "title": name_value,
                "distance": dist_to_user,
                "latitude": float(latitude_value),
                "longitude": float(longitude_value)
            })
        sorted_coffee_shops = sorted(coffee_shops, key=get_distance)
        nearest_five_coffee_shops = sorted_coffee_shops[:5]
        map_center = (user_coords[0], user_coords[1])
        m = folium.Map(location=map_center, zoom_start=15)
        folium.Marker(
            location=map_center,
            popup="Вы здесь",
            icon=folium.Icon(color="blue", icon="user")
        ).add_to(m)
        for coffee in nearest_five_coffee_shops:
            coffee_location = (coffee["latitude"], coffee["longitude"])
            folium.Marker(
                location=coffee_location,
                popup=f"{coffee['title']} ({round(coffee['distance'], 2)} км)",
                icon=folium.Icon(color="red", icon="coffee")
            ).add_to(m)
        map_file = base_path / 'index.html'
        m.save(map_file)


if __name__ == "__main__":
    main()

