from tkinter import *
from tkinter import ttk


# Using one frame
root = Tk()
frame = Frame(root)
frame.pack()
first = Label(frame, text="First label")
first.pack()
second = Label(frame, text="Second label")
second.pack()
third = Label(frame, text="Third label")
third.pack()


root.mainloop()



