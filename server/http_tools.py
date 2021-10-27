import email
import socket

from http.client import responses
from io import StringIO
from typing import Tuple, Dict

from server.types import Response


def send_response(conn: socket.socket, response: Response):
    message = f'HTTP/1.0 {response["code"]} {responses[response["code"]]}\n\n{response["message"]}'.encode()
    conn.send(message)


def parse_request(request_string: str) -> Tuple[str, str, str, Dict]:
    # Pop the first line so we only process headers
    first_line, headers = request_string.split('\r\n', 1)

    # Parse the first line
    method, route, protocol = first_line.split(" ")
    assert protocol == "HTTP/1.1", "The server currently supports HTTP only"

    # Construct a message from the request string
    message = email.message_from_file(StringIO(headers))

    # Construct a dictionary containing the headers
    headers_dict = dict(message.items())

    return first_line, method, route, headers_dict
