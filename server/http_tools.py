import email
import socket

from http.client import responses
from io import StringIO
from typing import Tuple, Dict

from server.types import Response, TYPE_REQUEST_METHOD


def send_response(conn: socket.socket, response: Response):
    code, message = response["code"], response["message"]
    message = f'HTTP/1.0 {code} {responses[code]}\n\n{response["message"]}'
    conn.sendall(message.encode())
    conn.close()


def parse_request(request_string: str) -> Tuple[str, TYPE_REQUEST_METHOD, str, Dict]:
    # Pop the first line so we only process headers
    headline, headers = request_string.split('\r\n', 1)

    # Parse the first line
    method, route, protocol = headline.split(" ")
    assert protocol == "HTTP/1.1", "The server currently supports HTTP only"

    # Construct a message from the request string
    message = email.message_from_file(StringIO(headers))

    # Construct a dictionary containing the headers
    headers_dict = dict(message.items())

    return headline, method, route, headers_dict
