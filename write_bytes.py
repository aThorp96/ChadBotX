import serial

# "./outputs/bytes.txt"
# "/dev/ttyUSB0"
def write(filename, port, baudrate=115200, bytesize=serial.EIGHTBITS):
    f = open(filename, "rb")
    rx = serial.Serial(port, baudrate, bytesize)

    next_byte_is_instruction = False

    while bytes is not None:
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
        else:
            # Normal byte
            f.write(chr(byte))

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

def terminate(f, rx):
    f.close()
    rx.close()
    quit()
