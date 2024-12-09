ciphertext_core = bytes.fromhex("a9 f6 34 08 42 2a 9e 1c 0c 03 a8 08 94 70 bb 8d aa dc 6d 7b 24 ff 7f 24 7c da 83 9e 92 f7 07 1d")

#
ciphertext = b"\x9b\xc2\x0592\x12\x80>%#\xd8'\x8aB\x8f\xa2\x8f\xa9Uz\x03\xd2_\x17X\xb6\xad\xb1\xfd\xd5)1I\xa4\x89\x024Lt\x064\t\xe2\xf3\x8f\xac;\xeb\xc1j4\xf1\xfb?h\xf2\x05\xcf3_\xf6\x83\xc2\x17\x9b\xc2\x0592\x12\x80>%#\xd8'\x8aB\x8f\xa2\x8f\xa9Uz\x03\xd2_\x17X\xb6\xad\xb1\xfd\xd5)1I\xa4\x89\x024Lt\x064\t\xe2\xf3\x8f\xac;\xeb\xc1j4\xf1\xfb?h\xf2\x05\xcf3_\xf6\x83\xc2\x17"
cleartext = b"A"*128

print(len(ciphertext))
print(len(cleartext))

def xor_bytes(bytes1, bytes2):
    # Use zip to pair corresponding bytes, apply XOR, and return a new bytes object
    return bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

cryptostream = xor_bytes(ciphertext, cleartext)
print("Cryptostream: ", cryptostream.hex())
print(xor_bytes(cryptostream, ciphertext_core))