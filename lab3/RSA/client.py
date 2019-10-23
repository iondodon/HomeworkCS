import socket
import pickle
import rsa


class Client:
    def __init__(self, socket):
        self.RSA = rsa.RSA()
        self.keys = self.RSA.get_key_pair()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8989))

        request = {'action': 'get_public_key'}
        self.socket.send(pickle.dumps(request))

        partner_pub_key_bin = self.socket.recv(1024)
        partner_pub_key = pickle.loads(partner_pub_key_bin)

        print(partner_pub_key)

        self.socket.close()


if __name__ == '__main__':
    client = Client(socket)
