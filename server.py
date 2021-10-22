import socket

from logger import logger


class Server:

    def __init__(self):
        self.logger = logger(f"server")
        self.socket = socket.socket(
            socket.AF_INET,         # AF_INET refers to the address-family ipv4
            socket.SOCK_STREAM      # The SOCK_STREAM means connection-oriented TCP protocol
        )

    def listen(self, port: int):
        """
        Puts the server into listening mode. This allows the server to listen to incoming connections
        :return:
        """
        """
        Binds the server to a specific IP and port so that it can listen to incoming requests on that IP and port
        :return:
        """
        # Empty string instead of IP makes the server listen to requests coming from other computers on the network
        self.socket.bind(("", port))
        self.logger.info(f"Socket is bound to {port}")

        self.socket.listen(5)
        self.logger.info(f"Server is listening on {port}")

        # a forever loop until we interrupt it or
        # an error occurs
        while True:
            # Establish connection with client.
            c, addr = self.socket.accept()
            print('Got connection from', addr)

            # send a thank you message to the client. encoding to send byte type.
            c.send('Thank you for connecting'.encode())

            # Close the connection with the client
            c.close()

            # Breaking once connection closed
            break


def main():
    server = Server()
    server.listen(12345)


if __name__ == '__main__':
    main()
