#!/usr/bin/env python

from socket import *
from code import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = ">"
    if not data:
        break
    tcpCliSock.send(data.encode("utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))

tcpCliSock.close()
