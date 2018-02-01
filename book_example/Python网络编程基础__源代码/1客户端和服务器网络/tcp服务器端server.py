#!/usr/bin/env python
# Simple Server - Chapter 1 - server.py
import socket

host = ''                               # Bind to all interfaces
port = 51423

#建立socket套接字描述符
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." \
      % port

while 1:
    #获取文件描述符
    clientsock, clientaddr = s.accept()
    #文件描述符
    clientfile = clientsock.makefile('rw', 0)
    #问文件描述符
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    #读文件描述符
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.close()
    clientsock.close()

