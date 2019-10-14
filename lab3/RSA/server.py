import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8989))
server_socket.listen()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.close()
