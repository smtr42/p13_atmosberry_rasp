import requests
from datetime import datetime, time
from logger import logger
import time

from get_weather import get_data
import sys
import pytz
import os
import utils
from set_env import set_env


@utils.object_exception_handler
def utcisoformat(dt):
    """
    Return a datetime object in ISO 8601 format in UTC, without microseconds
    or time zone offset other than 'Z', e.g. '2011-06-28T00:00:00Z'. Useful
    for making Django DateTimeField values compatible with the
    jquery.localtime plugin.
    """
    TZ = pytz.timezone("Europe/Paris")
    # Convert datetime to UTC, remove microseconds, remove timezone, convert to string
    return (
        TZ.localize(dt.replace(microsecond=0))
        .astimezone(pytz.utc)
        .replace(tzinfo=None)
        .isoformat()
        + "Z"
    )


def get_token():
    """Return the token used to authenticate on the website """
    return os.getenv("token")


def send_data():
    """Send data to the website with openweather data. """
    try:
        token = get_token()
        while True:
            data = get_data()
            if data:
                header = {"Authorization": f"Token {token}"}
                temp = data.get("temp")
                timestamp = utcisoformat(datetime.now())
                logger.info(f"Sending data {temp} at {timestamp}")
                data = {
                    "sensor_type": "T",
                    "device": "Raspberry",
                    "measure": temp,
                    "timestamp": timestamp,
                    "name": "BMP280",
                }
                response = requests.post(
                    "http://www.simteiva.fr/api/v1/", headers=header, data=data
                )
            time.sleep(10)
    except KeyboardInterrupt:
        logger.warning("Interrupted script execution with keyboard")
        sys.exit()


if __name__ == "__main__":
    set_env()
    send_data()