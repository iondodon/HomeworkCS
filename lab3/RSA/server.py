import socket
import pickle
import rsa


class Server:
    def __init__(self):
        self.RSA = rsa.RSA()
        self.keys = self.RSA.get_key_pair()

        self.client_pub_key = None
        self.client_socket = None

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8989))

    def exchange_keys(self, request):
        self.client_pub_key = request['client_pub_key']
        response_dict = {'type': "server_pub_key", 'public_key': self.keys[0]}
        response_dict_bin = pickle.dumps(response_dict)
        self.client_socket.send(response_dict_bin)

    def send_response_message(self, message_int_list):
        encrypted_response_message_int_list = self.RSA.rsa_encrypt(self.client_pub_key, message_int_list)
        response = {'type': "response_message", 'message': encrypted_response_message_int_list}
        response_bin = pickle.dumps(response)
        self.client_socket.send(response_bin)

    def show_message(self, encrypted_message_int_list):
        decrypted_message_int_list = self.RSA.rsa_decrypt(self.keys[1], encrypted_message_int_list)
        print(self.RSA.to_string(decrypted_message_int_list))
        self.send_response_message(decrypted_message_int_list)

    def process_request(self, request):
        if request['type'] == "get_server_pub_key":
            self.exchange_keys(request)
        elif request['type'] == "send_message":
            self.show_message(request['message'])

    def listen(self):
        self.socket.listen()
        client_socket, client_addr = self.socket.accept()
        self.client_socket = client_socket

        while True:
            request_dict_bin = client_socket.recv(1024)
            request: dict = pickle.loads(request_dict_bin)
            self.process_request(request)

    def close_socket(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server()
    server.listen()
    server.close_socket()
