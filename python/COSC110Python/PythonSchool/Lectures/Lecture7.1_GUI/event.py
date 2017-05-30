
from tkinter import *
from tkinter import ttk


def handleEnter(event):
    label["text"] = "Mouse moved inside"

def handleLeave(event):
    label["text"] = "Mouse moved outside"

def handleClick(event):
    label["text"] = "Clicked left button"

def handleDoubleClick(event):
    label["text"] = "Double clicked"

def handleRightDrag(event):  #note the positions on coordinate grid
    label["text"] = "Right button drag to {}, {}".format(event.x, event.y)



root = Tk()
label = Label(root, text="Starting ... ")
label.grid() # adding it to default position to grid

# binding these functions to event
label.bind("<Enter>", handleEnter)
label.bind("<Leave>", handleLeave)
label.bind("<1>", handleClick) # left mouse button = button 1
label.bind("<Double-1>", handleDoubleClick)
label.bind("<B3-Motion>", handleRightDrag)

root.mainloop()