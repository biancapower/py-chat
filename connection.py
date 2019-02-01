import socket

class Connection():
    """Encapsulates a connection to a remote host"""

    def __init__(self, socket):

        self.socket = socket

    def connect(self): #???
        pass

    def send(self, bytes):
        """sends some data (a bytes object) to the other host"""
        self.socket.send(bytes)

    def receive(self):
        """recieves and returns some data (a bytes object) from the other host"""

        return self.socket.recv(1024)
