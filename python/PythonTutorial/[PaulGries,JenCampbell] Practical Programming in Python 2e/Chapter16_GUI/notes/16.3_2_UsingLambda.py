from tkinter import *
from tkinter import ttk


# The controller
'''
def clickUp():
    click(counter, 1)

def clickDown():
    click(counter, -1)
'''

def click(counterVariable, value):
    counterVariable.set(counterVariable.get() + value)



if __name__ == "__main__":

    root = Tk()

    # the model
    # note: counter is global variable made by defining it in main (bit like R prog)
    # note - not supposed to use them, use better way later on.
    counter = IntVar()
    counter.set(0)

    # The views
    frame = Frame(root)
    frame.pack()
    # user updating the button calls click, which updates counter variable, which displays as
    # the label.
    button = Button(frame, text="Click Up", command= lambda: click(counter, 1))
    button.pack()
    button = Button(frame, text="Click Down", command= lambda: click(counter, -1))
    button.pack()

    label = Label(frame, textvariable=counter)
    label.pack()


    print("starting value: ", counter.get())


    # start machinery!
    root.mainloop()



    print("ending value: ", counter.get())