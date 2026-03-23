import requests
from plyer import notification
import time


# USER INPUT

city = input("Enter city name: ")
refresh = int(input("Enter refresh interval (seconds): "))


# GET LATITUDE & LONGITUDE
def get_location(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    data = requests.get(url).json()

    if "results" not in data:
        print("City not found!")
        return None, None

    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    return lat, lon

lat, lon = get_location(city)
if not lat:
    exit()


# GET WEATHER

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data = requests.get(url).json()

    w = data.get("current_weather")
    if not w:
        return "Weather data not available"

    temp = w["temperature"]
    wind = w["windspeed"]

    return f"Temperature: {temp}°C\nWind: {wind} km/h"


# SHOW NOTIFICATION

def notify(msg):
    notification.notify(
        title=f"Weather Update - {city}",
        message=msg,
        timeout=5
    )


# MAIN LOOP

while True:
    info = get_weather(lat, lon)
    notify(info)
    time.sleep(refresh)
