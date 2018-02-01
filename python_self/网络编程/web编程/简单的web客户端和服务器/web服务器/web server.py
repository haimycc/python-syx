# -*- coding:utf-8 -*-
import socket

HOST, PORT = '127.0.0.1', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#绑定ip和端口号
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
#打印监听端口号
print('Serving HTTP on port %s ...' % PORT)
while True:
    #获取服务套接字
    client_connection, client_address = listen_socket.accept()
    #获取客户端请求
    request = client_connection.recv(1024)
    print(request)
    #获取服务器响应
    http_response = """
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
