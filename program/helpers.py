def b_t_t(barray):
    with open("../outputs/bytes.txt","w") as f:
        print(barray)
        for byte in barray:
#            print("printing : " + str(byte))
            print(type(byte))
            f.write(chr(byte))
    print("all done")

def t_t_b(filename):
    bytearray = bytes([])
    with open(filename, "rb") as f:
        for i, byte in enumerate(f.read()):
            bytearray.append(byte)

    return bytearray

arr = t_t_b('../TAS-inputs/regular.fm2')

f = open("regular.txt", "wb")
f.write(arr)
f.close()
