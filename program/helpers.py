def b_t_t(barray):
    with open("../outputs/bytes.txt","w") as f:
        print(barray)
        for byte in barray:
#            print("printing : " + str(byte))
            print(type(byte))
            f.write(chr(byte))
    print("all done")

def t_t_b(filename):
    bytearray = []
    with open(filename, "rb") as f:
        for i, byte in enumerate(f.read()):
            bytearray.append(byte)

    return bytearray

