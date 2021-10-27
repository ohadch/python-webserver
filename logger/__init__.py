import logging
from typing import Dict

_loggers: Dict = {}

LOG_MESSAGE_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'


def _get_console_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    return console_handler


def _get_file_handler(name: str, formatter: logging.Formatter) -> logging.FileHandler:
    # create console handler and set level to debug
    file_handler = logging.FileHandler(f"./logs/{name}.log")
    file_handler.setLevel(logging.DEBUG)

    # add formatter to console_handler
    file_handler.setFormatter(formatter)

    return file_handler


def logger(name: str) -> logging.Logger:
    if _loggers.get(name) is not None:
        return _loggers[name]

    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOG_MESSAGE_FORMAT)

    console_handler = _get_console_handler(formatter)
    file_handler = _get_file_handler(name, formatter)

    # add console_handler to logger
    _logger.addHandler(console_handler)
    _logger.addHandler(file_handler)

    # Monolith
    _loggers[name] = _logger

    return _logger
