import socket

from logger import logger
from server.request_handler import RequestHandler


class Server:

    def __del__(self):
        print("Closing the socket")
        self.socket.close()
        print("End")

    def __init__(self, handlers: [RequestHandler]):
        self.logger = logger(f"server")
        self.socket = socket.socket(
            socket.AF_INET,         # AF_INET refers to the address-family ipv4
            socket.SOCK_STREAM      # The SOCK_STREAM means connection-oriented TCP protocol
        )
        self.handlers: [RequestHandler] = handlers
        self.waiting_connections: int = 5

    def handle_request(self, connection, endpoint: str):
        for handler in self.handlers:
            if handler.endpoint == endpoint:
                response = handler.handle()
                connection.send(response)
                connection.close()

    def listen(self, port: int):
        """
        Puts the server into listening mode. This allows the server to listen to incoming connections
        :return:
        """
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
            try:
                # Establish connection with client.
                connection, address = self.socket.accept()
                self.logger.info(f'Got connection from {address}')
                self.handle_request(connection, address)
            except Exception as e:
                self.logger.error(f"Unknown exception occurred, exiting: {e}")
                exit(-1)
