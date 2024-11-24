with open("out.txt","wb") as outputFD:
    outputBuffer = bytearray(b"")
    outputBuffer += bytearray(b"_"*85)

    # hash.md5 checks define:
    outputBuffer[50] = ord("3")
    outputBuffer[51] = ord("A")

    outputBuffer[32] = ord("u")
    outputBuffer[33] = ord("l")

    outputBuffer[0] = ord("r")
    outputBuffer[1] = ord("u")

    outputBuffer[76] = ord("i")
    outputBuffer[77] = ord("o")

    # bitwise on basic operations
    outputBuffer[52] = 119
    outputBuffer[53] = 52
    outputBuffer[54] = 121
    outputBuffer[55] = 64

    outputBuffer[17] = 114
    outputBuffer[18] = 105
    outputBuffer[19] = 110
    outputBuffer[20] = 103

    outputBuffer[59] = 114
    outputBuffer[60] = 101
    outputBuffer[61] = 45
    outputBuffer[62] = 111

    outputBuffer[28] = 32
    outputBuffer[29] = 34
    outputBuffer[30] = 49
    outputBuffer[31] = 82

    outputBuffer[66] = 111
    outputBuffer[67] = 109
    outputBuffer[68] = 34
    outputBuffer[69] = 32

    outputBuffer[10] = 111
    outputBuffer[11] = 110
    outputBuffer[12] = 32
    outputBuffer[13] = 123

    outputBuffer[37] = 97
    outputBuffer[38] = 121
    outputBuffer[39] = 75
    outputBuffer[40] = 51

    outputBuffer[22] = 58
    outputBuffer[23] = 32
    outputBuffer[24] = 36
    outputBuffer[25] = 102

    outputBuffer[46] = 108
    outputBuffer[47] = 119
    outputBuffer[48] = 52
    outputBuffer[49] = 114

    outputBuffer[70] = 99
    outputBuffer[71] = 111
    outputBuffer[72] = 110
    outputBuffer[73] = 100

    outputBuffer[80] = 32
    outputBuffer[81] = 36
    outputBuffer[82] = 102
    outputBuffer[83] = 32

    outputBuffer[3] = 101
    outputBuffer[4] = 32
    outputBuffer[5] = 102
    outputBuffer[6] = 108

    outputBuffer[41] = 51
    outputBuffer[42] = 112
    outputBuffer[43] = 36
    outputBuffer[44] = 77

    # sha256 rules
    outputBuffer[14] = ord(" ")
    outputBuffer[15] = ord("s")

    outputBuffer[56] = ord("f")
    outputBuffer[57] = ord("l")

    # crc32 rules
    outputBuffer[8] = ord("r")
    outputBuffer[9] = ord("e")

    outputBuffer[34] = ord("e")
    outputBuffer[35] = ord("A")

    outputBuffer[63] = ord("n")
    outputBuffer[64] = ord(".")

    outputBuffer[78] = ord("n")
    outputBuffer[79] = ord(":")

    # uint8 remainings

    outputBuffer[58] = 97
    outputBuffer[36] = 68
    outputBuffer[27] = 61
    outputBuffer[65] = 99
    outputBuffer[45] = 97
    outputBuffer[74] = 105
    outputBuffer[75] = 116
    outputBuffer[2] = 108
    outputBuffer[7] = 97
    outputBuffer[21] = 115
    outputBuffer[16] = 116
    outputBuffer[26] = 32
    outputBuffer[84] = 125

    # now i can write indexing from outputBuffer[0] to outputBuffer[84]
    # need to write INTEGERS with size 0-255, both inclusive

    if len(outputBuffer) != 85:
        print("ERROR, INCORRECT OUTPUT LENGTH")
        exit(-1)
    print(len(outputBuffer))
    outputFD.write(outputBuffer)
