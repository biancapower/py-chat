import socket

import select


class Network():
    class Connection():
        """Encapsulates a connection to a remote host"""

        def __init__(self, socket):

            self.socket = socket

        def connect(self): #???
            pass

        def send(self, bytes):
            """sends some data (a bytes object) to the other host"""
            self.socket.send(bytes)

        def try_receive(self):
            """recieves and returns some data (a bytes object) from the other host"""

            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            # inputs_ready == [] if no connection available
            # inputs_ready == [self.socket] if a connection is available

            if len(inputs_ready) == 0:
                return None

            return self.socket.recv(1024)

    class Listener():
        """Encapsulates a thing listening for connections"""

        def __init__(self, port):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('0.0.0.0', port))
            self.socket.listen()

        def try_get_connection(self):
            """Tries to get an incoming Connection, returning it or None"""

            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            # inputs_ready == [] if no connection available
            # inputs_ready == [self.socket] if a connection is available

            if len(inputs_ready) == 0:
                return None

            (client_socket, dontcare) = self.socket.accept()

            return Network.Connection(client_socket)
