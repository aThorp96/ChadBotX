import tkinter
from tkinter import ttk, filedialog
import serial.tools.list_ports

root = tkinter.Tk()

portname = tkinter.StringVar(root, "Select port")
filename = tkinter.StringVar(root, "Test")


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

# Add widgets to window
ttk.Button(root, text="Choose file", command=pick_file).pack()
entry = ttk.Entry(root, textvariable=filename)
entry.pack()
ttk.Combobox(root, textvariable=portname, values=get_ports()).pack()

filename.set("hello")

root.mainloop()