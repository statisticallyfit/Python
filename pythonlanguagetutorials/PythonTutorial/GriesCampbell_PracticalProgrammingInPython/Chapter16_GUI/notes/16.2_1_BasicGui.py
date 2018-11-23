from tkinter import *
from tkinter import ttk


root = Tk()
label = Label(root, text="This is our label.")
label.pack() # note: crucial otherwise labels not displayed well (balnk in this case)

#note: updating text as program runs, like an add-on
label.config(text="Second label")
root.mainloop()