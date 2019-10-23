import socket
import pickle
import rsa


class Server:
    def __init__(self, socket):
        self.RSA = rsa.RSA()
        self.keys = self.RSA.get_key_pair()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8989))

    def send_public_key(self, client_socket):
        client_socket.send(pickle.dumps(self.keys[0]))

    def process_query(self, request, client_socket):
        if request['action'] == 'get_public_key':
            self.send_public_key(client_socket)

    def listen(self):
        self.socket.listen()

        while True:
            client_socket, client_addr = self.socket.accept()

            request_bin = client_socket.recv(1024)
            request: dict = pickle.loads(request_bin)

            self.process_query(request, client_socket)  #

    def close_socket(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server(socket)
    server.listen()
    server.close_socket()
