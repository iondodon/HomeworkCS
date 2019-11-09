import socket
import pickle
import rsa
import dsa


class Server:
    def __init__(self):
        self.RSA = rsa.RSA()
        self.DSA = dsa.DSA()
        self.keys = self.RSA.get_key_pair()

        self.client_pub_key = None
        self.client_dsa_pub_key = None
        self.dsa_p = None
        self.dsa_q = None
        self.dsa_g = None
        self.dsa_priv_key = None
        self.dsa_pub_key = None

        self.client_socket = None

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8989))

    def exchange_keys(self, request):
        self.client_pub_key = request['client_pub_key']
        self.client_dsa_pub_key = request['client_dsa_pub_key']
        self.dsa_p = request['dsa_p']
        self.dsa_q = request['dsa_q']
        self.dsa_g = request['dsa_g']
        self.dsa_priv_key, self.dsa_pub_key = self.DSA.generate_keys(self.dsa_g, self.dsa_p, self.dsa_q)
        response_dict = {
            'type': "exchange_keys",
            'server_public_key': self.keys[0],
            'server_dsa_pub_key': self.dsa_pub_key
        }
        response_dict_bin = pickle.dumps(response_dict)
        self.client_socket.send(response_dict_bin)

    def send_response_message(self, message_int_list):
        plain_message_string = self.RSA.to_string(message_int_list)
        plain_message_string_encoded = str.encode(plain_message_string, "ascii")
        dsa_r, dsa_s = self.DSA.sign(plain_message_string_encoded, self.dsa_p, self.dsa_q, self.dsa_g, self.dsa_priv_key)
        encrypted_response_message_int_list = self.RSA.rsa_encrypt(self.client_pub_key, message_int_list)
        response = {
            'type': "response_message",
            'message': encrypted_response_message_int_list,
            'signature': {'dsa_r': dsa_r, 'dsa_s': dsa_s}
        }
        response_bin = pickle.dumps(response)
        self.client_socket.send(response_bin)

    def show_message(self, request):
        encrypted_message_int_list = request['message']
        decrypted_message_int_list = self.RSA.rsa_decrypt(self.keys[1], encrypted_message_int_list)
        decrypted_message_string = self.RSA.to_string(decrypted_message_int_list)
        self.check_signature(decrypted_message_string, request['signature'])
        print(decrypted_message_string)
        self.send_response_message(decrypted_message_int_list)

    def check_signature(self, message, signature):
        if self.DSA.verify(
                str.encode(message, "ascii"),
                signature['dsa_r'],
                signature['dsa_s'],
                self.dsa_p, self.dsa_q, self.dsa_g,
                self.client_dsa_pub_key):
            print("Message is authentic!")
        else:
            print("Message is not authentic!")

    def process_request(self, request):
        if request['type'] == "exchange_keys":
            self.exchange_keys(request)
        elif request['type'] == "send_message":
            self.show_message(request)

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
