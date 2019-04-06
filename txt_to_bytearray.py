def txt_to_byte(filename):
    bytearray = []
    with open(filename, "rb") as f:
        for i, byte in enumerate(f.read()):
            bytearray.append(byte)

    return bytearray

print(txt_to_byte("../TAS-inputs/HappyLee_SMB_TAS.fm2"))
