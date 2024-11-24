import base64
import itertools

def xor_bytes(byte_string, xor_key):
    # Use itertools.cycle to repeat the xor_key as needed
    repeated_key = itertools.cycle(xor_key)
    x = list((a ^b) for a, b in zip(byte_string, repeated_key))
    return bytes(x)

# Hardcoded Base64 string
base64_string = "cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA=="

# Decode the Base64 string to get the original bytes
decoded_bytes = base64.b64decode(base64_string)
print(len(decoded_bytes))

# Another byte string to XOR with
xor_key = b"FlareOn2024"

# Perform XOR
xor_result = xor_bytes(decoded_bytes, xor_key)

# Print the XOR result
print(xor_result)
# If you want to print it as a Base64 string after XOR
encoded_result = base64.b64encode(xor_result)
print("XOR Result (Base64):", encoded_result.decode("utf-8"))

