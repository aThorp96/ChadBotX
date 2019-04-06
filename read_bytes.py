import serial

port = "/dev/ttyUSB0"
baudrate = 115200
bytesize = serial.EIGHTBITS
filename = "./TAS-inputs/no-lag-frames.txt"
f = open(filename, "rb")

rx = serial.Serial(port, baudrate, bytesize)

def read():
    # Read bytes from arduino
    
    # byte = f.read(1)

    next_byte_is_instruction = False

    while True:
        # Print each byte from serial data
        bytes = rx.read()
        byte = ord(bytes)

        if (byte == 0xFF):
            # Begin instruction
            next_byte_is_instruction = True

        elif (next_byte_is_instruction):
            # Recieved special instruction from arduino
            execute(byte)
            next_byte_is_instruction = False

def sendNextByte():
    byte = f.read(1)

    if not byte:
        # End of file
        rx.write(0xFF)
        rx.write(0xAA)
        terminate()

    else:
        print(byte)
        rx.write(byte)

def execute(byte):
    if (byte == 0xAA):
        # End of file
        terminate()
    elif (byte == 0xBB):
        print('testB')
        # Set mode read
    elif (byte == 0xCC):
        print('testC')
        # Set mode play (write)
    elif (byte == 0x00):
        print('test0')
        # Stop playing
    elif (byte == 0xDD):
        # Ready for bits
        sendNextByte()


def terminate():
    f.close()
    rx.close()
    quit()

read()