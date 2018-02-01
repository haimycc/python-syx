# Written by Vamei

import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = b'''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.png"/>
</html>
'''

# Read picture, put into HTTP format
f = open('./test.png','rb')
pic_content = b'''
HTTP/1.x 200 OK
Content-Type: image/png

'''
pic_content = pic_content + f.read()
f.close()

# Configure socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    method = request.decode('utf-8').split(' ')[0]
    src = request.decode('utf-8').split(' ')[1]
    print("method is ",method)
    print("src is ",src)

    # deal with GET method
    if method == 'GET':
        # ULR
        if src == '/test.png':
            content = pic_content
        else:
            content = text_content

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()
