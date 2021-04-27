import json
import os
import time
import traceback

from utils import object_exception_handler, setup_request


@object_exception_handler
def get_data():
    """Get data from openweather map to send met data as an example."""

    api_key = os.getenv("weather_token")
    city = "lyon"
    units = "metric"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    data = None
    try:
        req = setup_request()
        response = req.get(url)
        data = json.loads(response.text)
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]

        data = {"temp": temp, "P": pressure, "Hu": humidity}
    except ConnectionError:
        time.sleep(100)
    except Exception as err:
        print(f"error: {err} traceback : {traceback.format_exc()}")
    return data
