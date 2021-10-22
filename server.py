import socket
import sys
from logger import logger

PORT = 80


s = socket.socket(
    socket.AF_INET,         # AF_INET refers to the address-family ipv4
    socket.SOCK_STREAM      # The SOCK_STREAM means connection-oriented TCP protocol
)


def connect_to(host: str, port: int = PORT):
    try:
        logger("server").info(f"Resolving IP for {host}")
        host_ip = socket.gethostbyname(host)
        logger("server").info(f"IP for {host} is {host_ip}")
    except socket.gaierror:
        logger("server").info(f'Failed resolving the ip for "{host}"')
        sys.exit()

    logger("server").info(f"Connecting to {host_ip}")
    s.connect((host_ip, port))
    logger("server").info(f"Successfully connected to {host} on {host_ip}")


if __name__ == '__main__':
    connect_to("www.google.com")
