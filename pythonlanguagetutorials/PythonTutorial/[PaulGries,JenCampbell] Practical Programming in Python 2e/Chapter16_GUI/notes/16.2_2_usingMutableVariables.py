from tkinter import *
from tkinter import ttk


root = Tk()
data = StringVar()
# note: values in containers are set/get
data.set("Data to display")

# note: Label is better than configure because it knows when one of its
# variables changes and can change it as well (like a sticky memory)
label = Label(root, textvariable=data)
label.pack()


root.mainloop()