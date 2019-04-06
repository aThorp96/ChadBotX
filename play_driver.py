from gpiozero import LED
# R  L  D  U  T  S  B  A
# 12 16 20 21 6  13 19 21
R = LED(12)
L = LED(16)
D = LED(20)
U = LED(21)
T = LED(6)
S = LED(13)
B = LED(19)
A = LED(21)


def output(byte_array):
    for byte in byte_array:
        if 0x80 & byte != 0:
            R.on()
        else:
            R.off()
        if 0x40 & byte != 0:
            L.on()
        else:
            L.off()
        if 0x20 & byte != 0:
            D.on()
        else:
            D.off()
        if 0x10 & byte != 0:
            U.on()
        else:
            U.off()
        if 0x08 & byte != 0:
            T.on()
        else:
            T.off()
        if 0x04 & byte != 0:
            S.on()
        else:
            S.off()
        if 0x02 & byte != 0:
            B.on()
        else:
            B.off()
        if 0x01 & byte != 0:
            A.on()
        else:
            A.off()
