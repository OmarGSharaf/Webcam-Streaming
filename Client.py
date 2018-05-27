import socket
from Videofeed import Videofeed

class Client:
    def __init__(self, TCP_IP = "127.0.0.1", TCP_PORT = "8080", BUFFER_SIZE = 32768):
        self.BUFFER_SIZE = BUFFER_SIZE
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((TCP_IP, int(TCP_PORT)))
        self.vf = Videofeed("client", 0)
        self.vf.start()
        print "[INFO] Client connected to server[", TCP_IP, "] on port: ", TCP_PORT

    def connect(self):
        while True:
            data = self.vf.get_frame() 
            self.client_socket.send(data)           
        self.client_socket.close() 

if __name__ == "__main__":

    client = Client()
    client.connect()
	
