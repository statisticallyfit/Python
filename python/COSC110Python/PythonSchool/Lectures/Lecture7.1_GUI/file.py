from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = filedialog.askopenfile()
print(filename) # prints filename selected

filename = filedialog.asksaveasfilename()
print(filename)

dirname = filedialog.askdirectory()
print(dirname)



messagebox.showinfo(message = "Hello")
messagebox.askyesno(message = "Are you sure?", icon = "question", title="install")
