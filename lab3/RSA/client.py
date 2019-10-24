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

        self.partner_pub_key = None
        self.requesting_thread = None
        self.listening_thread = None
        self.threads = []

    def start_threads(self):
        self.threads = []
        self.requesting_thread = threading.Thread(target=self.request, args=())
        self.listening_thread = threading.Thread(target=self.listen, args=())
        self.threads.append(self.requesting_thread)
        self.threads.append(self.listening_thread)
        self.requesting_thread.start()
        self.listening_thread.start()

        for thread in self.threads:
            thread.join()

    def listen(self):
        while True:
            response_data_bin = self.socket.recv(1024)
            self.partner_pub_key = pickle.loads(response_data_bin)
            print(self.partner_pub_key)

    def request(self):
        while True:
            request_string_json = input()
            request_dict = json.loads(request_string_json)
            request_dict_binary = pickle.dumps(request_dict)
            self.socket.send(request_dict_binary)

    def close_socket(self):
        self.socket.close()


if __name__ == '__main__':
    client = Client()
    client.start_threads()
