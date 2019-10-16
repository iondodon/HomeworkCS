import socket
import pickle
import rsa

KEYS = rsa.get_key_pair()


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(('localhost', 8989))

    partner_pub_key_bin = socket.recv(1024)
    partner_pub_key = pickle.loads(partner_pub_key_bin)

    data = [5, 4, 3, 2, 1]
    data_encrypted = rsa.rsa_encrypt(partner_pub_key, data)
    data_encrypted_bin = pickle.dumps(data_encrypted)
    socket.send(data_encrypted_bin)

    socket.close()
