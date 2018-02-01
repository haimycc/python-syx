
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    #建立socket
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    #发送一行数据
    data = "hello,world\r\n"
    if not data:
        break
    #client发送消息给server
    tcpCliSock.send(data.encode("utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip().decode("utf-8"))
    tcpCliSock.close()