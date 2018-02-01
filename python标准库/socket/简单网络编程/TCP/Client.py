
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

#tcp client
tcpclient=socket(AF_INET,SOCK_STREAM)
tcpclient.connect(ADDR)

while True:
    data=">"
    if not data:
        break
    #client发送消息给server
    tcpclient.send(data.encode("utf-8"))
    #client接受消息
    data=tcpclient.recv(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))

tcpclient.close()
