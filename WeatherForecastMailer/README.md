This is a weather mailer built in Python :snake: Project is to send weather details to a customer list which has emails. 
The sent data will be the schedule for the day and the current weather forecast for the day.

## Project Requirements

+ Ensure you have **Python** installed, preferably Python 3+
+ **requests** module which will enable us to make http requests, This can be install using `pip` a Python package manager
    ```bash
    pip install requests
    ```
    The request module retrieves data in JSON, which makes it easier to parse the data received.
    An example of making a JSON request:
    ``` python
    >>> import requests
    >>> r = requests.get('https://api.github.com/events')
    >>> r.json()
    [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
    ```
    The request module comes with its own inbuilt json method which makes it easier to retrieve JSON data.
+ **API key from openweather.org.** This is necessary especially considering that you will need to make API requests to openweather. This key will be used for all API requests. Signing up is [free](https://openweathermap.org/). 
An example JSON response from openweather API is as follows:

    REQUEST:
    `http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=<YOUR API KEY COMES HERE>`

    RESPONSE
    `{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],
    "base":"cmc stations","main":{"temp":292.47,"pressure":1015,"humidity":64,"temp_min":291.15,"temp_max":293.71}, "wind":{"speed":6.7,"deg":210,"gust":11.8},"clouds":{"all":88},"dt":1472908819,"sys":{"type":1,"id":5091,"message":0    .0054,"country":"GB","sunrise":1472879862,"sunset":1472928019},"id":2643743,"name":"London","cod":200}`

+ **Text file (or JSON) with email addresses**, they do not have to be hundreds of them, just enough for testing.
+ **Text file (or JSON) with schedules**. These could be schedules of any kind you like.


### Project breakdown and structure

I have broken down this project to simple individual Python files, text and JSON files. It is recommended you break it down even more Pythonically. Also hide any API keys, APP ids and secrets in a separate file and import them into your Python script that will run the main method. Do not push this file to Github or any VCS you use. This should be kept secret. To do this, add a *.gitignore* file to your project and include the name that will contain all your scripts in here. This *.gitignore* file will be pushed to github

   1. __init__.py
        This is just an empty file notifying Python that this is a Python Package
   
   2. emailer.py
        This is the file that reads the emails from a text file or a JSON file

   3. weather.py
        Reads the JSON response from OpenWeather API. 
       
### Goal

Automate emailing such that we do not need to hardcode the email addresses or the overall function

## Functions used

This just describes the logic of the functions used.

+ __read_emails()__

This reads the email text file by opening it in `r` read mode and storing the file in a variable `email_file` for later retrieval. It is wrapped in a `try...except` block to check for any `FileNotFound` exceptions just in case the file is not there at all. After reading the file, we loop through the file using a `for` loop splitting each line at the comma seperator using the string method `str.split(separator)` and storing the email and the name in a tuple variable. After which we strip any white space from the name variable and store it as a value in the dictionary `emails` which we return.
    A JSON file could be preferably used as less checks can be performed on whitespace and also there will be no need to split the string.
    
+ __get_schedule()__:

This is used to retrieve the schedule from a text file. The schedule will be used to send the emails. The same operation used in `read_emails()` function is applied here, with the only differnce being that the sperator used is `-`
    
+ __get_current_weather_forecast()__:
   
   This obtains the current weather forecast of a particular place using the OpenWeather API.
   An example request of current weather in London, UK
   ``` python
   def get_current_weather_forecast():
        url = current_weather + "q=London,uk&" + key
        weather_req = requests.get(url=url)
        response = weather_req.json()
        return response
   ```
   The `requests.get(url)` returns an object which we use to get the JSON data, which is simply a dictionary in Python. 
   
   Output:
   ``` python
   {'base': 'cmc stations',
    'clouds': {'all': 88},
    'cod': 200,
    'coord': {'lat': 51.51, 'lon': -0.13},
    'dt': 1472907620,
    'id': 2643743,
    'main': {'humidity': 64,
          'pressure': 1015,
          'temp': 292.34,
          'temp_max': 293.71,
          'temp_min': 291.15},
    'name': 'London',
    'sys': {'country': 'GB',
         'id': 5091,
         'message': 0.004,
         'sunrise': 1472879861,
         'sunset': 1472928021,
         'type': 1},
    'weather': [{'description': 'light rain',
              'icon': '10d',
              'id': 500,
              'main': 'Rain'}],
    'wind': {'deg': 210, 'gust': 11.8, 'speed': 6.7}}
   ```
   