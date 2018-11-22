from tkinter import *
from tkinter import ttk


# Creating the widgets
root = Tk()
frame = Frame(root, width=400, height=400)
frame.grid()

image = PhotoImage(file="tux.gif")
label1 = Label(frame, image=image)
label2 = Label(frame, image=image)
label3 = Label(frame, image=image)
label4 = Label(frame, image=image)
label1.grid(column=1, row=2)
label2.grid(column=2, row=1)
label3.grid(column=2, row=3)
label4.grid(column=3, row=2)
button = Button(frame, text="Button")
button.grid(column=2, row=2, sticky=N)
button.grid(column=2, row=2, sticky=S)
button.grid(column=2, row=2, sticky=W)
button.grid(column=2, row=2, sticky=E)
button.grid(column=2, row=2, sticky=(N, E))
button.grid(column=2, row=2, sticky=(S, W))
button.grid(column=2, row=2, sticky=(N, S)) # takes up entire height of cell
button.grid(column=2, row=2, sticky=(E, W)) # takes up entire width of cell

button.grid(column=2, row=2, sticky=(N, S, E, W)) # takes up entire height of cell

# note: resizing doesn't move widgets at all by default
# need to use colconfig and rowconfig to resize weight

root.mainloop()