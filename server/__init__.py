import socket
import traceback
from typing import List

from logger import logger
from server.http_tools import parse_request, send_response
from server.request_handler import RequestHandler
from server.types import TYPE_REQUEST_METHOD, Response


class Server:

    def __del__(self):
        print("Closing the socket")
        self.socket.close()
        print("End")

    def __init__(self, handlers: List[RequestHandler]):
        self.logger = logger(f"server")
        self.socket = socket.socket(
            socket.AF_INET,         # AF_INET refers to the address-family ipv4
            socket.SOCK_STREAM      # The SOCK_STREAM means connection-oriented TCP protocol
        )
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.handlers: List[RequestHandler] = handlers
        self.waiting_connections: int = 5

    def listen(self, port: int):
        """
        Binds the server to a specific IP and port so that it can listen to incoming requests on that IP and port
        :return:
        """
        # Empty string instead of IP makes the server listen to
        # requests coming from other computers on the network.
        # If we would have passed 127.0.0.1 then it would have
        # listened to only those calls made within the local computer.
        self.socket.bind(("", port))
        self.logger.info(f"Socket is bound to {port}")

        # 5 here means that 5 connections are kept waiting if the server is
        # busy and if a 6th socket tries to connect then the connection is refused.
        self.socket.listen(self.waiting_connections)
        self.logger.info(f"Server is listening on {port}")

        # a forever loop until we interrupt it or
        # an error occurs
        while True:
            self._accept_connection()

    def _accept_connection(self):
        # Establish connection with client.
        conn, address = self.socket.accept()

        try:
            data = conn.recv(1024).decode("utf-8")
            headline, method, endpoint, headers = parse_request(data)
            self.logger.info(headline)

            self._handle_request(conn, method, endpoint, headers)
        except Exception as e:
            self.logger.error(f"Unknown exception occurred: {e}")
            print(traceback.format_exc())
            conn.close()

    def _handle_request(self, conn: socket.socket, method: TYPE_REQUEST_METHOD, endpoint: str, headers: dict):
        response: Response = {"code": 404, "message": "not found"}
        for handler in self.handlers:
            if handler.endpoint == endpoint and handler.method == method:
                response = handler.handle()
                break

        send_response(conn, response)

    @staticmethod
    def _parse_data(data: bytes):
        s = data.decode("utf-8")
        return s
