def byteArrayOut(fm2):
    with open(fm2) as f:
        f_array = f.readlines()

        results = []

        for line in f_array:
            if line[0] == '|':
                results.append(strToByte(line[3:11]))
	#outputs the array of bytes, one byte for each frame of input
        return bytes(results)

def strToByte(buttonString):
    #buttonString is a single line of the button inputs in the format of the .fm2
    count = 0

    for i, char in enumerate(buttonString):
        if buttonString[i] != '.': count += (2 ** (7 - i))

    return count # returns the buttons as a byte
    #R......A
    #10000001
    #X81


def byteToStr(byte):
    buttons = 'RLDUTSBA'
    binString = '{0:08b}'.format(byte)
    buttonString = ''

    for i, digit in enumerate(binString):
        if digit == '1':
            buttonString += buttons[i]
        else:
            buttonString += '.'

    return buttonString
BAO = byteArrayOut("../TAS-inputs/HappyLee_SMB_TAS.fm2")


print(BAO)
  
#print(byteToStr(0x88))

def generateFM2(byteArray):
    file = open('../outputs/output.fm2', 'w')

    metadata = {
        "version": input('Version (required): '),
        "emuVersion": input('Emulator version (required): '),
        "rerecordCount": input('Re-record count: '),
        "palFlag": input('Pal flag: '),
        "romFilename": input('ROM file name (required): '),
        "romChecksum": input('ROM Checksum (required): '),
        "guid": input('GUID (required): '),
        "fourscore": input('Fourscore: '),
        "microphone": input('Microphone: '),
        "port0": input('Port 0: '),
        "port1": input('Port 1: '),
        "port2": input('Port 2 (required): '),
        "FDS": input('FDS: '),
        "NewPPU": input('New PPU: '),
        "comment author": input('Comment: ')
    }

    for field, value in metadata.items():
        if bool(value):
            file.write(field + ' ' + value + '\n')
    
    for i, byte in enumerate(byteArray):
        prefix = '|1|' if i == 0 else '|0|'

        file.write(prefix + byteToStr(byte) + '|........||' + '\n')


generateFM2(BAO)
