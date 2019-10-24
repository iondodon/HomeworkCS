import socket
import pickle
import rsa


class Server:
    def __init__(self):
        self.RSA = rsa.RSA()
        self.keys = self.RSA.get_key_pair()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8989))

    def send_public_key(self, client_socket):
        response_dict = {'type': 'public_key', 'public_key': self.keys[0]}
        response_dict_bin = pickle.dumps(response_dict)
        client_socket.send(response_dict_bin)

    def decrypt_data(self, data_int_list):
        # print(self.RSA.to_string(data_int_list))
        decrypted_data_int_list = self.RSA.rsa_decrypt(self.keys[1], data_int_list)
        print(self.RSA.to_string(decrypted_data_int_list))

    def process_request(self, request, client_socket):
        if request['action'] == 'get_public_key':
            self.send_public_key(client_socket)
        elif request['action'] == 'send_data':
            self.decrypt_data(request['data'])

    def listen(self):
        self.socket.listen()
        client_socket, client_addr = self.socket.accept()
        while True:
            request_dict_bin = client_socket.recv(1024)
            request: dict = pickle.loads(request_dict_bin)
            self.process_request(request, client_socket)

    def close_socket(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server()
    server.listen()
    server.close_socket()
