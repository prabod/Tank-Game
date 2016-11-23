import threading
import socket
import sys


class ServerListner(threading.Thread):
    def __init__(self, serverIP, serverPort):
        super(ServerListner, self).__init__()
        # Server IP
        self.serverIP = serverIP
        # Server Port
        self.serverPort = serverPort
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.components = []
        print "ininit"

    def run(self):
        # Bind the socket to the port
        server_address = (self.serverIP, self.serverPort)
        print >> sys.stderr, 'starting up on %s port %s' % server_address
        self.sock.bind(server_address)
        # Listen for incoming connections
        self.sock.listen(5)

        while True:
            # Wait for a connection
            print >> sys.stderr, 'waiting for a connection'
            connection, client_address = self.sock.accept()
            try:
                #print >> sys.stderr, 'connection from', client_address
                data = connection.recv(4096*16)
                #print >> sys.stderr, 'received "%s"' % data
                self.notifyComponents(data)
            except socket.error, ex:
                print ex
            finally:
                connection.close()

    def notifyComponents(self,data):
        for component in self.components:
            component.parse(data)

    def registerComponent(self,component):
        self.components.append(component)

