import socket
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def recv_all(sock, length):
    """Receive exactly `length` bytes from the socket."""
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))  # Get what's remaining
        if not packet:
            # Connection closed or error
            raise ConnectionError("Connection closed before receiving all data")
        data += packet
    return data

ciphertext = b'\x12\x94x\xd6{jO\x10I\x8cl\xee\xd0\xb5;\xce\xd9+\xe4>@\xa6\x11\xeb\x82\x0fj\x8c|(\x1e\x1aq\xad\x17\xfbi\x9f\xb8\xe1\xcf\xee\x08\xd7\x97\x0cW\xd2I\xbd\t\xe6\xc9\x181\x95\x02"\xb3\xb5$\xa4\xd4d\x12\x94x\xd6{jO\x10I\x8cl\xee\xd0\xb5;\xce\xd9+\xe4>@\xa6\x11\xeb\x82\x0fj\x8c|(\x1e\x1aq\xad\x17\xfbi\x9f\xb8\xe1\xcf\xee\x08\xd7\x97\x0cW\xd2I\xbd\t\xe6\xc9\x181\x95\x02"\xb3\xb5$\xa4\xd4d'
cleartext = b"A"*128

def xor_bytes(bytes1, bytes2):
    # Use zip to pair corresponding bytes, apply XOR, and return a new bytes object
    return bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

cryptostream = xor_bytes(ciphertext, cleartext)

# Function to generate a fixed ChaCha20 key and nonce
def get_fixed_chacha20_key_nonce():
    #key = b'\x22' * 32  # 32 bytes key of all 2s
#    key = bytes.fromhex("94 3d f6 38 a8 18 13 e2 de 63 18 a5 07 f9 a0 ba 2d bb 8a 7b a6 36 66 d0 8d 11 a6 5e c9 14 d6 6f".strip(" "))
#    nonce = bytes.fromhex("f2 36 83 9f 4d cd 71 1a 52 86 29 55".strip(" "))
    key = bytes.fromhex("8d ec 91 12 eb 76 0e da 7c 7d 87 a4 43 27 1c 35 d9 e0 cb 87 89 93 b4 d9 04 ae f9 34 fa 21 66 d7")
    nonce = bytes.fromhex("11 11 11 11 11 11 11 11 11 11 11 11")

    #nonce = b'\x11' * 12  # 12 bytes nonce of all 0s
    return key, nonce

# Function to encrypt/decrypt using ChaCha20
def chacha20_encrypt_decrypt(key, nonce, data):
    nonce = b'\x00\x00\x00\x00' + nonce
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(('10.0.2.15', 1337))
    server_socket.listen(1)
    print('Server listening on 10.0.2.15:1337')

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection accepted from {addr}")

        # Get the fixed ChaCha20 key and nonce
        key, nonce = get_fixed_chacha20_key_nonce()

        # Send the 32-byte key and 12-byte nonce
        client_socket.sendall(key)
        client_socket.sendall(nonce)

        # Prepare the string to send
        string_to_send = b"/a.txt"
        string_length = len(string_to_send)

        # Send a 4-byte uint32 (length of the string)
        client_socket.sendall(struct.pack('!I', string_length))

        # Send the actual string
        client_socket.sendall(string_to_send)

        # Wait to receive a 4-byte uint32 (length of buffer to receive)
        buffer_length_data = recv_all(client_socket, 4)
        print("Received: ", buffer_length_data)
        buffer_length = int.from_bytes(buffer_length_data, byteorder="little")
        print("Receiving n bytes: ", buffer_length)
        # Receive the encrypted buffer
        encrypted_message = recv_all(client_socket, buffer_length)

        # Decrypt the message using ChaCha20
        print(f"Received bytes: {encrypted_message}")
        decrypted_message = xor_bytes(encrypted_message,cryptostream)
        print(f"Decrypted message: {decrypted_message}")

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    main()
