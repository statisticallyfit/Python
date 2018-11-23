from tkinter import *
from tkinter import ttk


root = Tk()
frame = Frame(root)
frame.pack() # note: each widget has method pack that tells parent to resize itself as necessary.
var = StringVar()
label = Label(frame, textvariable=var)
label.pack()
entry = Entry(frame, textvariable=var)
entry.pack()

# note: we have a StringVar. When we get input via the entry, we update the value
# of the variable. Since var is associated with Label, that new entry value
# will appear as the label as well, reflecting what is currently in the entry.

root.mainloop()