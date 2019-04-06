import tkinter
from tkinter import ttk, filedialog, messagebox
import serial.tools.list_ports

root = tkinter.Tk()
ser = serial.Serial()
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS

# Define constants for mode selection
MODE_RECORD = 1
MODE_PLAYBACK = 2

# Define gui state
portname = tkinter.StringVar(root, "")
filename = tkinter.StringVar(root, "")
mode = tkinter.IntVar(root, 0)


def pick_file():
    # Open file picker and return name of file selcted

    newfilename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Movie files","*.fm2"),("all files","*.*")))
    # tkinter.StringVar(root, filename)
    filename.set(newfilename)
    

def get_ports():
    # Get list of com ports
    # https://pythonhosted.org/pyserial/tools.html

    ports = serial.tools.list_ports.comports()
    ports_str = []

    for port in ports:
        ports_str.append(port.device)

    return ports_str

def start():
    opt_mode = mode.get()
    opt_filename = filename.get()
    opt_port = portname.get()

    if (not opt_mode or not opt_filename or not opt_mode):
        return messagebox.showwarning("Error", "Invalid input")

    if (opt_mode == MODE_PLAYBACK):
        print("playback " + opt_filename + " " + opt_port)
    elif (opt_mode == MODE_RECORD):
        print("record " + opt_filename + " " + opt_port)

# Add widgets to window
ttk.Button(root, text="Choose file", command=pick_file).pack(pady=(10, 7))

ttk.Label(root, text="File name:").pack()
entry = ttk.Entry(root, textvariable=filename).pack(pady=(0, 2))

ttk.Label(root, text="Port:").pack()
ttk.Combobox(root, textvariable=portname, values=get_ports()).pack(pady=(0, 2), padx=(10, 10))

ttk.Radiobutton(root, text="Record", variable=mode, value=1).pack(pady=(5, 2))
ttk.Radiobutton(root, text="Playback", variable=mode, value=2).pack(pady=(2, 5))

ttk.Button(root, text="Start", command=start).pack(pady=(2, 10))

root.mainloop()