import json
import requests

WEATHER_API_KEY = '449983ee3206dc0bb76305c70871dd24'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_current_weather(location):
    # Fetch current weather data using the API
    params = {
        "q": location,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(WEATHER_API_URL, params=params)
    weather_data = response.json()

    # Update the weather_data.json file
    with open('data/weather_data.json', 'w') as weather_file:
        json.dump(weather_data, weather_file)

    return weather_data