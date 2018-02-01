#!/usr/bin/env python
# Echo client with deadlock - Chapter 3 - echoclient.py

import socket, sys
port = 51423
host = 'localhost'

data = "x" * 10485760                  # 10MB of data

#socket客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
byteswritten = 0
while byteswritten < len(data):
    #写数据
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data))
    #发送数据
    byteswritten += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
    sys.stdout.flush()
#关闭套接字链接
s.shutdown(1)

print "All data sent."
while 1:
    #接收数据
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
