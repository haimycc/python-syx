#!/usr/bin/env python
# Simple Gopher Client with basic error handling - Chapter 1
# gopherclient2.py

import socket, sys

port = 51423
host = sys.argv[1]
filename = sys.argv[2]
#建立链接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #建立链接，检查服务器是否ok
    s.connect((host, port))
except Exception, e:
    print("Error connecting to server: %s" % e)
    sys.exit(1)

#发送消息
s.sendall(filename + "\r\n")

while 1:
    #返回响应
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
    
