import threading
from typing import Callable

from logger import logger
from server.types import TYPE_REQUEST_METHOD, Response


class RequestHandler:

    def __init__(self, method: TYPE_REQUEST_METHOD, endpoint: str, action: Callable[..., Response]):
        self.method: TYPE_REQUEST_METHOD = method
        self.endpoint = endpoint
        self.action = action

    def handle(self):
        logger(f"RequestHandler_thread_{threading.get_ident()}").info("Handling request")
        return self.action()
