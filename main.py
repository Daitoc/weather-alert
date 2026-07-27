import requests

def get_rain_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "precipitation_probability_max",
        "timezone": "America/Sao_Paulo"

    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

lat = float(input("Enter your city's latitude: "))
lon = float(input("Enter your city's longitude: "))

data = get_rain_forecast(lat, lon)

rain_chances = data["daily"]["precipitation_probability_max"]
tomorrow_rain_chance = rain_chances[1]

if tomorrow_rain_chance > 50:
    print(f"It should rain tomorrow {rain_chances[1]}%")
else:
    print(f"It shouldn't rain tomorrow {rain_chances[1]}%")
