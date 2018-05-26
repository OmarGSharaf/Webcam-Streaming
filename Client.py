import socket

class Client:
    def __init__(self, TCP_IP = "127.0.0.1", TCP_PORT = "8080", BUFFER_SIZE = 1024):
        self.BUFFER_SIZE = BUFFER_SIZE
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((TCP_IP, int(TCP_PORT)))
        print "[INFO] Client connected to server[", TCP_IP, "] on port: ", TCP_PORT

    def connect(self):
        for i in range (1,512):
            self.client_socket.send(str(i))
            THREAD_INDEX = self.client_socket.recv(self.BUFFER_SIZE)
            print "Client[%s] sent:   %s\n" %(THREAD_INDEX, i),
            
        self.client_socket.close() 

if __name__ == "__main__":

    client = Client()
    client.connect()
	
