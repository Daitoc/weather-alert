import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

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

def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city_name,
        "count": 1,
        "language": "pt",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    city = data["results"][0]
    lat = city["latitude"]
    lon = city["longitude"]
    return lat, lon

def send_email(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email_address, email_password)
    server.sendmail(email_address, email_address, message)
    server.quit()


city_name = input("Enter the name of your city: ")

lat, lon = get_coordinates(city_name)

data = get_rain_forecast(lat, lon)

rain_chances = data["daily"]["precipitation_probability_max"]
tomorrow_rain_chance = rain_chances[1]

if tomorrow_rain_chance > 50:
    send_email(f"It should rain tomorrow {rain_chances[1]}%")
else:
    send_email(f"It shouldn't rain tomorrow {rain_chances[1]}%")
