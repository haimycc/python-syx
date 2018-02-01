#-*- coding: UTF-8 -*-

from SocketServer import (TCPServer,StreamRequestHandler)
from time import ctime


HOST=""
PORT=8888
ADDR=(HOST,PORT)

class MyREQESTHANDLER(SocketServer.StreamRequestHandler):
    def handle(self):
        print("...connected from:", self.client_address)
        self.wfile.write("[%s] %s" % (ctime(),self.rfile.readline()))

tcpServer=TCPServer(ADDR,MyREQESTHANDLER)
tcpServer.serve_forever()