import requests
from datetime import datetime

MY_LAT = 32.085300
MY_LONG = 34.781769
MY_KEY = "64dcfb3d413cae76fdbe6f12bf3c7e07"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
for hour in weather_data["hourly"][:12]:
    if int((str(hour["weather"][0]["id"])[0])) < 8:
        print("bring an umbrella")
        break