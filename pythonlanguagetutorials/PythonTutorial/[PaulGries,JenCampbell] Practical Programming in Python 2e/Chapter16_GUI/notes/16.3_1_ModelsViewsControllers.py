from tkinter import *
from tkinter import ttk

# The controller
def click():
    counter.set(counter.get() + 1)


if __name__ == "__main__":
    root = Tk()

    # the model
    counter = IntVar()
    counter.set(0)

    # The views
    frame = Frame(root, height=400, width=600)
    frame.pack()

    # user updating the button calls click, which updates counter variable, which displays as
    # the label.
    button = Button(frame, text="Click", command=click, padx=50, pady=50)
    button.pack()

    label = Label(frame, textvariable=counter)
    label.pack()



    # start machinery!
    root.mainloop()



    print("ending value: ", counter.get())