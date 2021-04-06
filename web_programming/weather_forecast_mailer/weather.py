import requests
from WeatherForecastMailer import constants

key = constants.open_weather_key
current_weather = constants.base_url


def get_current_weather_forecast(town):
    url = current_weather + "q=" + town + "&units=metric" + key
    weather_req = requests.get(url=url)
    response = weather_req.json()

    # Parse the JSON response, cast floats to integers, convert to strings
    description = response["weather"][0]["description"]
    temp = response['main']['temp']

    temp_min, temp_max = str(int(response['main']['temp_min'])) + " degrees Celsius", str(
        int(response['main']['temp_max'])) + " degrees Celsius"

    output = "Current weather forecast for " + town + " today is " + description + " with a high of " + temp_max \
             + " and min of " + temp_min
    return output
