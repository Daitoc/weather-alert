import requests


latitude = -23.55
longitude = -46.63

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "precipitation_probability_max",
    "timezone": "America/Sao_Paulo"

}

response = requests.get(url, params=params)

data = response.json()

rain_chances = data["daily"]["precipitation_probability_max"]

tomorrow_rain_chance = rain_chances[1]

if tomorrow_rain_chance > 50:
    print(f"It should rain tomorrow {rain_chances[1]}%")
else:
    print(f"It shouldn't rain tomorrow {rain_chances[1]}%")
