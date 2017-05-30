from tkinter import *
from tkinter import ttk


if __name__ == "__main__":
    root = Tk()

    # the model
    var = StringVar()

    # the views
    frame = Frame(root)
    frame.pack()


    label = Label(frame, textvariable=var, font=("Calibri", 9), bg="cyan", fg="magenta")
    label.pack()
    entry = Entry(frame, textvariable=var, font=("Times", 14, "italic"), bg="black", fg="orange")
    entry.pack()
    button = Button(frame, text="Random", font="Tahoma", bg="blue", fg="red")
    button.pack()

    root.mainloop()
