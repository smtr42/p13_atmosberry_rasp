import functools
from logger import logger
import traceback


def object_exception_handler(f):
    """
    A function wrapper for catching all exceptions and logging them
    """

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
