from tkinter import *
from tkinter import ttk


class Counter:
    """ A simple counter GUI using object-oriented programming. """

    def __init__(self, parent):
        """Create the GUI """

        # Framework
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S)) # not visible
        self.frame.columnconfigure(0, weight=1) #help what do these mean?
        self.frame.rowconfigure(0, weight=1)

        # Model
        self.state = IntVar()
        self.state.set(1)

        # Label displaying current state
        self.label = Label(self.frame, textvariable=self.state)
        self.label.grid(row=0, column=1, sticky=N)

        # Buttons to control app.
        self.up = Button(self.frame, text="Up", command=self.upClick)
        self.up.grid(row=1, column=0, sticky=(N, W))
        self.down = Button(self.frame, text="Down", command=self.downClick)
        self.down.grid(row=2, column=0, sticky=(S, W))
        self.quit = Button(self.frame, text="Quit", command=self.quitClick)
        self.quit.grid(row=2, column=2, stick=(S, E))

        # adding padding around everything
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5) # padx: puts space between rows, pady: space between columns.


    def upClick(self):
        self.state.set(self.state.get() + 1)

    def downClick(self):
        self.state.set(self.state.get() - 1)

    def quitClick(self):
        self.parent.destroy()




if __name__ == "__main__":
    root = Tk()
    app = Counter(root)
    root.mainloop()