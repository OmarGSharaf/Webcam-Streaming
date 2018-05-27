import socket, threading, sys
from Videofeed import Videofeed

threadLimiter = threading.BoundedSemaphore(5)

class ClientThread(threading.Thread):

    def __init__(self, client_socket, addr, THREAD_INDEX ,BUFFER_SIZE = 65536):
        self.THREAD_INDEX = THREAD_INDEX
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE
        self.vf = Videofeed(str(self.THREAD_INDEX))
        print "[INFO] connection received from: %s\n" %(self.addr[1]),

    def run(self):
            threadLimiter.acquire()
            try:
                while True:
                    data = b''
                    while True:
                        part = self.client_socket.recv(self.BUFFER_SIZE)
                        data += part
                        if len(part) < self.BUFFER_SIZE: break
                    self.vf.set_frame(data)

            except socket.error, e: 
                print "\n[CLIENT THREAD ERROR] ", e
                sys.exit(True)
            finally:
                self.client_socket.close()
                threadLimiter.release()
                print "[INFO] Socket closed on port: %s\n" %(self.addr[1]),
                print "[INFO] Thread %s is released\n" %(self.THREAD_INDEX),
