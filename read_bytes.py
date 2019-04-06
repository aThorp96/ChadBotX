import serial

f = open("./outputs/bytes.txt", "w")
rx = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=serial.EIGHTBITS, timeout=1.0)

bytes = rx.read()

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

def terminate():
    f.close()
    rx.close()
    quit()

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
        execute(byte)
        next_byte_is_instruction = False
    else:
        # Normal byte
        f.write(chr(byte))

