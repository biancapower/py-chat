import socket

from connection import Connection

class Listener():
    """Encapsulates a thing listening for connections"""

    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('0.0.0.0', port))
        self.socket.listen()

    def get_connection(self):
        """Waits for and returns an incoming Connection"""
        (client_socket, dontcare) = self.socket.accept()

        return Connection(client_socket)
