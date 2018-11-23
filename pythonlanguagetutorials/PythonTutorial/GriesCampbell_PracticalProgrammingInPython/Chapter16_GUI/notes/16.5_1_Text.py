from tkinter import *
from tkinter import ttk


def cross(textVar):
    textVar.insert(INSERT, 'X')

if __name__ == "__main__":
    root = Tk()

    frame = Frame(root)
    frame.pack()

    text = Text(frame, height=3, width=10)
    text.grid(row=1, column=5)
    #text.pack()

    button = Button(frame, text='Add', command = lambda: cross(text))
    button.grid(row=2, column=5)
    #button.pack()

    # adding padding around everything
    #for child in frame.winfo_children():
     #   child.grid_configure(padx=5, pady=5) # padx: puts space between rows, pady: space between columns.

    #root.bind("<Return>", cross)
    root.mainloop()

