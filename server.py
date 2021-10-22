import socket
import sys
import logging

PORT = 80

logging.basicConfig(filename='./logs/all.log', encoding='utf-8', level=logging.DEBUG)

s = socket.socket(
    socket.AF_INET,         # AF_INET refers to the address-family ipv4
    socket.SOCK_STREAM      # The SOCK_STREAM means connection-oriented TCP protocol
)


def connect_to(host: str, port: int = PORT):
    try:
        logging.info(f"Resolving IP for {host}")
        host_ip = socket.gethostbyname(host)
        logging.info(f"IP for {host} is {host_ip}")
    except socket.gaierror:
        logging.info(f'Failed resolving the ip for "{host}"')
        sys.exit()

    logging.info(f"Connecting to {host_ip}")
    s.connect((host_ip, port))
    logging.info(f"Successfully connected to {host} on {host_ip}")


if __name__ == '__main__':
    connect_to("www.google.com")
