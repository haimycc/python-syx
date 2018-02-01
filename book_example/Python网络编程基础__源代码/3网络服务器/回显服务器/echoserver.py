#!/usr/bin/env python
# Echo Server - Chapter 3 - echoserver.py
import socket, traceback

host = ''                               # Bind to all interfaces
port = 51423

#socket套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        #服务套接字
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    # Process the connection

    try:
        print "Got connection from", clientsock.getpeername()
        while 1:
            #获取client的请求数据
            data = clientsock.recv(4096)
            if not len(data):
                break
            #回显
            clientsock.sendall(data)
    #如果有其他异常
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close the connection
    #关闭close socket链接
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
