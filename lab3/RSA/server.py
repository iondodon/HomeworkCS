import socket
import pickle
import rsa

KEYS = rsa.get_key_pair()


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.bind(('localhost', 8989))
    socket.listen()

    client_socket, client_addr = socket.accept()

    self_pub_key_bin = pickle.dumps(KEYS[0])
    client_socket.send(self_pub_key_bin)

    encrypted_data_bin = client_socket.recv(1024)
    print(encrypted_data_bin)
    encrypted_data = pickle.loads(encrypted_data_bin)
    print(encrypted_data)
    decrypted_data = rsa.rsa_decrypt(KEYS[1], encrypted_data)
    print(decrypted_data)

    socket.close()
