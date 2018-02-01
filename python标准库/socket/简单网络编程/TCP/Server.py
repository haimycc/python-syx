#!/user/bin/env python
#-*- coding: UTF-8 -*-

from socket import *
from time import ctime


HOST=""
PORT=8888
BUFSIZE=1024
ADDR=(HOST,PORT)

#建立soket链接
SERVER_SOCKET=socket(AF_INET,SOCK_STREAM)
SERVER_SOCKET.bind(ADDR)
SERVER_SOCKET.listen(5)

while True:
    print("waiting for connection...")
    #获取服务套接字
    SERVER_CONNECT,CLIENT_ADDR=SERVER_SOCKET.accept()
    print("...connected from:",CLIENT_ADDR)
    while True:
        #服务套接字获取字节缓冲区
        data=SERVER_CONNECT.recv(BUFSIZE)
        if not data:
            break
        #发送时间给client
        SERVER_CONNECT.send("[%s] %s" % (ctime(),data))
    #关闭服务套接字
    SERVER_CONNECT.close()
#关闭监听套接字
SERVER_SOCKET.close()


