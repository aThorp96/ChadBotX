import tkinter
from tkinter import ttk, filedialog
import serial.tools.list_ports

root = tkinter.Tk()

# Define constants for mode selection
MODE_RECORD = 1
MODE_PLAYBACK = 2

# Define gui state
portname = tkinter.StringVar(root, "Select port")
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
    if (mode.get() == MODE_PLAYBACK):
        print("playback " + filename.get() + " " + portname.get())
    elif (mode.get() == MODE_RECORD):
        print("record " + filename.get() + " " + portname.get())

# Add widgets to window
ttk.Button(root, text="Choose file", command=pick_file).pack(pady=(10, 2))

entry = ttk.Entry(root, textvariable=filename).pack(pady=(2, 2))

ttk.Combobox(root, textvariable=portname, values=get_ports()).pack(pady=(2, 2), padx=(10, 10))

ttk.Radiobutton(root, text="Record", variable=mode, value=1).pack(pady=(2, 2))
ttk.Radiobutton(root, text="Playback", variable=mode, value=2).pack(pady=(2, 2))

ttk.Button(root, text="Start", command=start).pack(pady=(2, 10))

root.mainloop()