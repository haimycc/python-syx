#-*- coding: UTF-8 -*-

from socket import *

HOST=""
PORT=8888
BUSIZE=1024
ADDR=(HOST,PORT)
#建立udp socket套接字
udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    data=">"
    if not data:
        break
    #发送消息给udp server
    udp_client.sendto(data.encode("utf-8"),ADDR)
    #从udp server获取内容
    data,ADDR=udp_client.recvfrom(BUSIZE)
    if not data:
        break
    print(data.decode("utf-8"))

udp_client.close()