from tkinter import *
from tkinter import ttk




def recolor(widget, r, g, b):
    color = "#"
    for var in (r, g, b):
        # note: if int value of either red/green/blue is not zero, then put
        # note - the color code FF for primary red/green/blue, else put zero (it's unchecked)
        color += "FF" if var.get() else "00"
        # note: color code must have six digits: __, __, __ (amount of red, green, blue)
    widget.config(bg=color) # config given widget's background (label) to be the color.


if __name__ == "__main__":
    root = Tk()

    frame = Frame(root)
    frame.pack()
    red = IntVar()
    green = IntVar()
    blue = IntVar()

    for (name, var) in (('R', red), ('G', green), ('B', blue)):
        check = Checkbutton(frame, text=name, variable=var)
        check.pack(side="left")

    label = Label(frame, text="[                 ]")
    label.pack(side="left")
    button = Button(frame, text="Update", command= lambda: recolor(label, red, green, blue))
    button.pack(side="left")


    root.mainloop()