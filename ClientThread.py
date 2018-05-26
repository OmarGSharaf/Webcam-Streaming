import socket, threading, sys
threadLimiter = threading.BoundedSemaphore(5)

class ClientThread(threading.Thread):

    def __init__(self, client_socket, addr, THREAD_INDEX ,BUFFER_SIZE = 20):
        self.THREAD_INDEX = THREAD_INDEX
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE
        print "[INFO] connection received from: %s\n" %(self.addr[1]),

    def run(self):
            threadLimiter.acquire()
            try:
                for x in range (1,512):
                    data = self.client_socket.recv(self.BUFFER_SIZE)
                    print "       THREAD[%s] received:   %s   From %s \n" %(self.THREAD_INDEX, data, self.addr),
                    self.client_socket.send(str(self.THREAD_INDEX))

                print "[INFO] Socket closed on port: %s\n" %(self.addr[1]),
                print "[INFO] Thread %s is released\n" %(self.THREAD_INDEX),
                self.client_socket.close()
            except socket.error, e: 
                print "\n[ERROR] ", e
                sys.exit(True)
            finally:
                threadLimiter.release()
