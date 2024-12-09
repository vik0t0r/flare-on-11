# THIS DOES NOT WORK FOR SOME REASON

from tqdm import tqdm
from collections import Counter
import math
import string
import base64
ciphertext = b'\x12\x94x\xd6{jO\x10I\x8cl\xee\xd0\xb5;\xce\xd9+\xe4>@\xa6\x11\xeb\x82\x0fj\x8c|(\x1e\x1aq\xad\x17\xfbi\x9f\xb8\xe1\xcf\xee\x08\xd7\x97\x0cW\xd2I\xbd\t\xe6\xc9\x181\x95\x02"\xb3\xb5$\xa4\xd4d\x12\x94x\xd6{jO\x10I\x8cl\xee\xd0\xb5;\xce\xd9+\xe4>@\xa6\x11\xeb\x82\x0fj\x8c|(\x1e\x1aq\xad\x17\xfbi\x9f\xb8\xe1\xcf\xee\x08\xd7\x97\x0cW\xd2I\xbd\t\xe6\xc9\x181\x95\x02"\xb3\xb5$\xa4\xd4d'
cleartext = b"A"*128

print(len(ciphertext))
print(len(cleartext))

def xor_bytes(bytes1, bytes2):
    # Use zip to pair corresponding bytes, apply XOR, and return a new bytes object
    return bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))


#cryptostream = xor_bytes(ciphertext, cleartext)


#cryptostream = bytes.fromhex("a9 f6 34 08 42 2a 9e 1c 0c 03 a8 08 94 70 bb 8d aa dc 6d 7b 24 ff 7f 24 7c da 83 9e 92 f7 07 1d")
cryptostream = b"\x9b\xc2\x0592\x12\x80>%#\xd8'\x8aB\x8f\xa2\x8f\xa9Uz\x03\xd2_\x17X\xb6\xad\xb1\xfd\xd5)1I\xa4\x89\x024Lt\x064\t\xe2\xf3\x8f\xac;\xeb\xc1j4\xf1\xfb?h\xf2\x05\xcf3_\xf6\x83\xc2\x17\x9b\xc2\x0592\x12\x80>%#\xd8'\x8aB\x8f\xa2\x8f\xa9Uz\x03\xd2_\x17X\xb6\xad\xb1\xfd\xd5)1I\xa4\x89\x024Lt\x064\t\xe2\xf3\x8f\xac;\xeb\xc1j4\xf1\xfb?h\xf2\x05\xcf3_\xf6\x83\xc2\x17"


print(cryptostream.hex())


########### start bruteforce
def shannon_entropy(block):
    if not block:
        return 0
    block_length = len(block)
    frequency = Counter(block)
    entropy = -sum((count / block_length) * math.log2(count / block_length) for count in frequency.values())
    return entropy

# Function to determine if the entropy is low
def is_low_entropy(block, threshold=5):  # Set threshold for low entropy
    entropy = shannon_entropy(block)
    return entropy < threshold

key = bytes.fromhex("94 3d f6 38 a8 18 13 e2 de 63 18 a5 07 f9 a0 ba 2d bb 8a 7b a6 36 66 d0 8d 11 a6 5e c9 14 d6 6f".strip(" "))
nonce = bytes.fromhex("f2 36 83 9f 4d cd 71 1a 52 86 29 55".strip(" "))

def is_ascii_printable(block):
    return all(chr(b) in string.printable for b in block)

posible_start_points = []

parcialstream = bytes([
    0x28, 0xf8, 0x2f, 0x8b, 0xae, 0x03, 0xd7, 0x7c, 0x2c, 0x58, 0xe2, 0x80, 0xe2, 0x1c, 0x71, 0x67,
    0x23, 0x3c, 0x9b, 0xde, 0xbc, 0x91, 0xe6, 0x0b, 0xac, 0x1f, 0xde, 0x8b, 0x18, 0x0c, 0x4c, 0x03,
    0xd6, 0xd8, 0x7a, 0xfe, 0x8b, 0x50, 0x79, 0xe4, 0xf5, 0x3b, 0x07, 0x00, 0x81, 0x75, 0x31, 0x23,
    0x2c, 0x86, 0x2f, 0x72, 0x16, 0x2d, 0x5e, 0x50, 0x9f, 0x8b, 0xaa, 0x58, 0x75, 0xe3, 0x1c, 0x29
])

try:
    with open("sshd.core.93794.0.0.11.1725917676", 'rb') as f:
        file_data = f.read()
        for start in tqdm(range(len(file_data)), desc="Decrypting", unit="byte"):


            block = file_data[start:start+128]
            if len(block) < 128:
                print("Not enough data:",block)
                break

            decrypted_block = xor_bytes(block,cryptostream)
            if b"@fl" in decrypted_block:#if is_low_entropy(decrypted_block):
                print(f"Possible start point: {start}")
                posible_start_points.append(start)
                print(f"Decrypted text: {decrypted_block}")
                print("-" * 50)

    print(posible_start_points)
except Exception as e:
    print(f"EXCEPTION: {e}")
    print(posible_start_points)
