import socket
import pickle
import rsa
import threading
import json


class Client:
    def __init__(self):
        self.RSA = rsa.RSA()
        self.keys = self.RSA.get_key_pair()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8989))

        self.server_pub_key = None
        self.requesting_thread = None
        self.listening_thread = None
        self.threads = []

    def start_threads(self):
        self.threads = []
        self.listening_thread = threading.Thread(target=self.listen, args=())
        self.threads.append(self.listening_thread)
        self.requesting_thread = threading.Thread(target=self.request, args=())
        self.threads.append(self.requesting_thread)
        self.listening_thread.start()
        self.requesting_thread.start()

        for thread in self.threads:
            thread.join()

    def show_response(self, response_dist):
        encrypted_response_message = response_dist['message']
        decrypted_response_message = self.RSA.rsa_decrypt(self.keys[1], encrypted_response_message)
        print(self.RSA.to_string(decrypted_response_message))

    def process_response(self, response_dist):
        if response_dist['type'] == "server_pub_key":
            self.server_pub_key = response_dist['public_key']
        elif response_dist['type'] == "response_message":
            self.show_response(response_dist)

    def encrypt_message(self, request_dict):
        if request_dict['type'] == "send_message":
            data_int_list = self.RSA.to_int_list(request_dict['message'])
            data_encrypted_int_list = self.RSA.rsa_encrypt(self.server_pub_key, data_int_list)
            request_dict['message'] = data_encrypted_int_list
        return request_dict

    def request(self):
        self.exchange_keys()
        while True:
            request_string_json = input()
            request_dict = json.loads(request_string_json)
            request_dict = self.encrypt_message(request_dict)
            request_dict_binary = pickle.dumps(request_dict)
            self.socket.send(request_dict_binary)

    def exchange_keys(self):
        if not self.server_pub_key:
            new_request_dict = {'type': "get_server_pub_key", "client_pub_key": self.keys[0]}
            new_request_dict_bin = pickle.dumps(new_request_dict)
            self.socket.send(new_request_dict_bin)

    def listen(self):
        while True:
            response_dict_bin = self.socket.recv(1024)
            response_dict = pickle.loads(response_dict_bin)
            self.process_response(response_dict)

    def close_socket(self):
        self.socket.close()


if __name__ == '__main__':
    # { "type": "send_message", "message": "ionnnn" }
    client = Client()
    client.start_threads()
