from tkinter import *
from tkinter import ttk


def change(widget, colors):
    '''
    Update the foreground color of a widget to show the RGD color value
    stored in a dictionary or tuple with keys 'red', 'green', and 'blue'.
    widget: widget whose color we change for background
    colors: dict or tuple of colors with keys "red, green, blue"
    return: None (because widget is an object and gets changed in memory)
    '''
    newVal = "#"
    for name in ('red', 'green', 'blue'):
        newVal += colors[name].get()
    widget['bg'] = newVal



if __name__ == "__main__":
    root = Tk()

    frame = Frame(root)
    frame.pack()
    frame.grid()

    # initialize = set text entry widgets for red, green, blue, storing variables.
    colors = {}
    for (name, color) in (('red', '#FF0000'),
                          ('green', '#00FF00'),
                          ('blue', "#0000FF")):
        colors[name] = StringVar()
        colors[name].set('00')
        entry = Entry(frame, textvariable=colors[name], bg=color, fg="white")
        entry.pack()


    # display current color
    #frame.configure(bg="#FFFFFF")
    current = Label(frame, text='   RESULT   ', bg='#FFFFFF', fg="#FFFFFF", font="bold")
    current.pack()

    # give user a way to trigger color update
    update = Button(frame, text="Update", command = lambda: change(current, colors))
    update.pack()


    root.mainloop()