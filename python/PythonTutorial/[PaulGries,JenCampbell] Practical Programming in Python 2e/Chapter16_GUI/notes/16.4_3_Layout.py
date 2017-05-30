from tkinter import *
from tkinter import ttk



if __name__ == "__main__":
    root = Tk()
    frame = Frame(root)
    frame.grid(row=0, column=0, rowspan=10, columnspan=10)

    label = Label(frame, text="Name")
    label.grid(row=0, column=0)
    entry = Entry(frame)
    entry.grid(row=1, column=1)

    root.mainloop()
