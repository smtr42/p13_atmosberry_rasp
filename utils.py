import functools
import traceback

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from logger import logger

DEFAULT_TIMEOUT = 5  # seconds


def object_exception_handler(f):
    """A function wrapper for catching all exceptions and logging them."""

    @functools.wraps(f)
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except IndexError as error:
            logger.error(
                f"IndexError Error: {error} traceback : {traceback.format_exc()}"
            )
        except KeyError as error:
            logger.error(
                f"KeyError Error: {error} traceback : {traceback.format_exc()}"
            )
        except NameError as error:
            logger.error(
                f"NameError Error: {error} traceback : {traceback.format_exc()}"
            )
        except SyntaxError as error:
            logger.error(
                f"SyntaxError Error: {error} traceback : {traceback.format_exc()}"
            )
        except TypeError as error:
            logger.error(
                f"TypeError Error: {error} traceback : {traceback.format_exc()}"
            )
        except RuntimeError as error:
            logger.error(
                f"RuntimeError Exception {error} traceback : {traceback.format_exc()}"
            )
        except Exception as error:
            logger.error(
                f" {f.__name__} requests UNEXPECTED FAILURE {error} traceback : {traceback.format_exc()}"
            )

    return inner


class TimeoutHTTPAdapter(HTTPAdapter):
    """A class setting up a timeout for requests."""

    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def setup_request():
    """A function returning a reauests session with custom timeout and
    retries."""
    retries = Retry(
        total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
    )
    req = requests.Session()
    req.mount("https://", TimeoutHTTPAdapter(max_retries=retries))
    req.mount("http://", TimeoutHTTPAdapter(max_retries=retries))
    return req
