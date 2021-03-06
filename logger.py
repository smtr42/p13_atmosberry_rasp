import logging


def setup_logger():
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler("file.log")
    f_handler.setLevel(logging.ERROR)
    f_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    return logger


logger = setup_logger()
