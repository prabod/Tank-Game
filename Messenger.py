import socket
import sys


class Messenger:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, message, ServerIP, port):
        # Connect the socket to the port where the server is listening
        server_address = (ServerIP, port)
        print >> sys.stderr, 'connecting to %s port %s' % server_address
        self.sock.connect(server_address)
        try:
            # Send data
            print >> sys.stderr, 'sending "%s"' % message
            self.sock.sendall(message)
        finally:
            print >> sys.stderr, 'closing socket'
            self.sock.close()
