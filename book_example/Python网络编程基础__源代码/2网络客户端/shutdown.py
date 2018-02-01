#!/usr/bin/env python
# Error Handling Example With Shutdown - Chapter 2

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    #建立socket套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating socket: %s" % e
    sys.exit(1)

# Try parsing it as a numeric port number.

try:
    #端口号
    port = int(textport)
except ValueError:
    # That didn't work.  Look it up instread.
    try:
        #获取服务对于的端口号
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)

try:
    #建立tcp链接
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)

print "sleeping..."
time.sleep(10)
print "Continuing."

try:
    #发送http请求
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)

try:
    #shutdown关闭写段
    s.shutdown(1)
except socket.error, e:
    print "Error sending data (detected by shutdown): %s" % e
    sys.exit(1)

while 1:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)
    
