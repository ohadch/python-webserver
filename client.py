# Import socket module
import socket


def request():
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    # receive data from the server and decoding to get the string.
    response = s.recv(1024).decode()

    # close the connection
    s.close()

    return response


def main():
    response = request()
    print("response:", response)


if __name__ == '__main__':
    main()
