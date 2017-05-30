from tkinter import *
from tkinter import ttk


# Using two frames
root = Tk()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root, borderwidth=4, relief=GROOVE)
frame2.pack()
first = Label(frame1, text='First label')
first.pack()
second = Label(frame2, text="Second label")
second.pack()
third = Label(frame2, text="Third Label")
third.pack()


root.mainloop()