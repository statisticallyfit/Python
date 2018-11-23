from tkinter import *
from tkinter import ttk
import tkinter.filedialog as dialog


def save(root, text):
    data = text.get("0.0", END)
    filename = dialog.asksaveasfilename(parent=root, filetypes=[('Text', '*.txt')],
                                        title="Save as...")
    writer = open(filename, 'w')
    writer.write(data)
    writer.close()

def quit(root):
    root.destroy()



if __name__ == "__main__":
    root = Tk()
    text = Text(root)
    text.pack()

    menuBar = Menu(root)
    fileMenu = Menu(menuBar)
    fileMenu.add_command(label="Save", command= lambda: save(root, text))
    fileMenu.add_command(label="Quit", command= lambda: quit(root))

    menuBar.add_cascade(label="File", menu=fileMenu)
    root.config(menu=menuBar)

    root.mainloop()