import serial

rx = serial.Serial('/dev/ttyUSB1', 115200)

read_byte = rx.read()

while read_byte is not None:
    # Print each byte from serial data
    read_byte = rx.read()
    print(ord(read_byte))

rx.close()