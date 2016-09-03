import requests
from WeatherForecastMailer import constants

key = constants.open_weather_key
current_weather = constants.base_url


def get_current_weather_forecast():
    url = current_weather + "q=London,uk&units=metric" + key
    weather_req = requests.get(url=url)
    response = weather_req.json()
    return response