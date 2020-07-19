class basicOperations():
    def __init__(self, BUFOR=1024):
        self.BUFOR = BUFOR
    def send(self, socket, message):
        socket.sendall(self)