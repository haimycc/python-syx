#-*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST=""
PORT=8888
BUFSIZE=1024
ADDR=(HOST,PORT)
#获取udp socket
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ADDR)

while True:
    print("waiting for message..")
    #从udp socket上获取消息
    data, addr = udp_server.recvfrom(BUFSIZE)
    send_data='[%s] %s' % (ctime(), data.decode("utf-8"))
    #发送消息给udp server
    udp_server.sendto(send_data.encode("utf-8"), addr)
    print("...received from and returned to:",addr)

udp_server.close()