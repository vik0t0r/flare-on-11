import zlib
import itertools
import string


def generate_crc32_for_2char_strings():
    # Generate all possible 2-character strings (from printable ASCII characters)
    chars = string.printable  # Printable ASCII characters
    combinations = itertools.product(chars, repeat=2)

    # Iterate through each combination and compute its CRC32
    for combination in combinations:
        input_string = ''.join(combination)
        crc_value = zlib.crc32(input_string.encode())

        yield (input_string, crc_value)


# Run the function
generate_crc32_for_2char_strings()

for input, crc32 in generate_crc32_for_2char_strings():
    if crc32 == 0x61089c5c:
        print(hex(crc32), input)
    if crc32 == 0x5888fc1b:
        print(hex(crc32), input)

    if crc32 == 0x66715919:
        print(hex(crc32), input)

    if crc32 == 0x7cab8d64:
        print(hex(crc32), input)