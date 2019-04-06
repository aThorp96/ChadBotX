import serial

f = open("./outputs/bytes.txt", "w")
rx = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=serial.EIGHTBITS, timeout=1.0)

bytes = rx.read()

while bytes is not None:
    # Print each byte from serial data
    bytes = rx.read()
    print(chr(ord(bytes)))
    f.write(chr(ord(bytes)))

f.close()
rx.close()