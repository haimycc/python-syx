# Written by Vamei
# Simple HTTPsERVER

import socketserver
from http.server import SimpleHTTPRequestHandler

HOST = ''
PORT = 8000

# Create the server, SimpleHTTPRequestHander is pre-defined handler in SimpleHTTPServer package
server = socketserver.TCPServer((HOST, PORT), SimpleHTTPRequestHandler)

# Start the server
server.serve_forever()