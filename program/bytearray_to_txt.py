 def b_t_t(barray):
    with open("../outputs/bytes.txt") as f:
        for byte in barray:
            print("printing : " + byte)
            f.write(byte)
    print("all done")

       
