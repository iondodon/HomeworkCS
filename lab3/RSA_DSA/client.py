import socket
import pickle
import rsa
import threading
import dsa


class Client:
    def __init__(self):
        self.RSA = rsa.RSA()
        self.DSA = dsa.DSA()
        self.keys = self.RSA.get_key_pair()

        print("Client RSA private key: ", self.keys[1])
        print("Client RSA public key: ", self.keys[0])
        print("==================================================================")

        N = 160
        L = 1024

        self.dsa_p, self.dsa_q, self.dsa_g = self.DSA.generate_params(L, N)
        self.dsa_priv_key, self.dsa_pub_key = self.DSA.generate_keys(self.dsa_g, self.dsa_p, self.dsa_q)
        print("Client DSA private key: ", self.dsa_priv_key)
        print("Client DSA public key: ", self.dsa_pub_key)
        print("==================================================================")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8989))

        self.server_pub_key = None
        self.server_dsa_pub_key = None
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

    def check_signature(self, plain_message, signature):
        print("The signature: ", signature)
        if self.DSA.verify(
                str.encode(plain_message, "ascii"),
                signature['dsa_r'],
                signature['dsa_s'],
                self.dsa_p, self.dsa_q, self.dsa_g,
                self.server_dsa_pub_key):
            print("Message is authentic!")
        else:
            print("Message is not authentic!")
        print("==================================================================")

    def show_response(self, response_dist):
        encrypted_response_message = response_dist['message']
        print("Encrypted echo message: ", encrypted_response_message)
        decrypted_response_message = self.RSA.rsa_decrypt(self.keys[1], encrypted_response_message)
        print("Decrypted echo message: ", decrypted_response_message)
        decrypted_response_message_string = self.RSA.to_string(decrypted_response_message)
        self.check_signature(decrypted_response_message_string, response_dist['signature'])
        print("Decrypted echo message: ", decrypted_response_message_string)
        print("==================================================================")

    def process_response(self, response_dist):
        if response_dist['type'] == "exchange_keys":
            self.server_pub_key = response_dist['server_public_key']
            self.server_dsa_pub_key = response_dist['server_dsa_pub_key']
            print("Server RSA public key: ", self.server_pub_key)
            print("Server DSA public key: ", self.server_dsa_pub_key)
            print("==================================================================")
        elif response_dist['type'] == "response_message":
            self.show_response(response_dist)

    def encrypt_sign_message(self, request_dict):
        if request_dict['type'] == "send_message":
            message = str.encode(request_dict['message'], "ascii")
            dsa_r, dsa_s = self.DSA.sign(message, self.dsa_p, self.dsa_q, self.dsa_g, self.dsa_priv_key)
            request_dict['signature'] = {'dsa_r': dsa_r, 'dsa_s': dsa_s}
            data_int_list = self.RSA.to_int_list(request_dict['message'])
            data_encrypted_int_list = self.RSA.rsa_encrypt(self.server_pub_key, data_int_list)
            request_dict['message'] = data_encrypted_int_list
        return request_dict

    def request(self):
        self.exchange_keys()
        while True:
            message = input()
            request_dict = {'type': "send_message", 'message': message}
            request_dict = self.encrypt_sign_message(request_dict)
            request_dict_binary = pickle.dumps(request_dict)
            self.socket.send(request_dict_binary)

    def exchange_keys(self):
        if not self.server_pub_key:
            new_request_dict = {
                'type': "exchange_keys",
                'client_pub_key': self.keys[0],
                'client_dsa_pub_key': self.dsa_pub_key,
                'dsa_p': self.dsa_p,
                'dsa_q': self.dsa_q,
                'dsa_g': self.dsa_g
            }
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
    client = Client()
    client.start_threads()
