import serial

def read(filename="./TAS-inputs/no-lag-frames.txt", port="/dev/ttyUSB0"):
    # Read bytes from arduino
    
    f = open(filename, "rb")
    rx = serial.Serial(port=port, baudrate=115200, bytesize=serial.EIGHTBITS)

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
            execute(byte, f, rx)
            next_byte_is_instruction = False

def sendNextByte(f, rx):
    byte = f.read(1)

    if not byte:
        # End of file
        rx.write(0xFF)
        rx.write(0xAA)
        terminate(f, rx)

    else:
        print(byte)
        rx.write(byte)

def execute(byte, f, rx):
    if (byte == 0xAA):
        # End of file
        terminate(f, rx)
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
        sendNextByte(f, rx)


def terminate(f, rx):
    f.close()
    rx.close()
    quit()