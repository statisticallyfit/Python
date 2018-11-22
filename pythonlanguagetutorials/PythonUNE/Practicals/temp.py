
from tkinter import *
from tkinter import ttk
#import Image, ImageTk

root = Tk()
frame = ttk.Frame(root, width=600, height=400, padding=5)
frame.grid()


# ABOUT FRAMES

for k, v in frame.configure().items():
    print(k, v)
frame.configure(borderwidth = 5)
frame.configure(relief="solid")
# or simpler instead of using configure
frame["relief"] = "flat"
frame["relief"] = "solid"
frame["relief"] = "raised"
frame["relief"] = "sunken"
frame["relief"] = "ridge"
frame["relief"] = "groove"




# ABOUT LABELS:
label = Label(frame, text="label")
label.grid() # telling it to display (resized to be small)
label["text"] = "Hello COSC110" # configuring
variable = StringVar()
label["textvariable"] = variable # empty value, empty string
variable.set("Hello, setting a variable")
variable.set(variable.get() + "\nThis is a new line.")
label["justify"] = "left" # is by default
label["justify"] = "right"
label["justify"] = "center"



root.mainloop()