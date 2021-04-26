import requests
import json
import traceback
import time
from utils import object_exception_handler
import os


@object_exception_handler
def get_data():
    """Get data from openweather map to send met data
    as an example"""

    api_key = os.getenv("weather_token")
    city = "lyon"
    units = "metric"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    data = None
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        print(data)
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]

        data = {"T": temp, "P": pressure, "Hu": humidity}
    except ConnectionError:
        time.sleep(100)
    except Exception as err:
        print(f"error: {err} traceback : {traceback.format_exc()}")
    return data
