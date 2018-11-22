from tkinter import *
from tkinter import ttk



# Creating the widgets
root = Tk()
content = ttk.Frame(root, padding = (3, 3, 12, 12)) # note padding
# another frame in the above content frame
frame = Frame(content, borderwidth=5, relief="sunken", width=200, height=100)





def okClickShowName():
    nameVar.set(nameEntry.get())


# Creating variable
nameVar = StringVar()



nameLabel = Label(content, text="Name: ")
nameShow = Label(content, textvariable=nameVar)
nameEntry = Entry(content)

oneVar = BooleanVar()
twoVar = BooleanVar()
threeVar = BooleanVar()
oneVar.set(True)
twoVar.set(False)
threeVar.set(True)

oneCheck = Checkbutton(content, text="One", variable=oneVar, onvalue=True, offvalue=False)
twoCheck = Checkbutton(content, text="Two", variable=twoVar, onvalue=True, offvalue=False)
threeCheck = Checkbutton(content, text="Three", variable=threeVar, onvalue=True, offvalue=False)

okButton = Button(content, text="Okay", command=okClickShowName)
cancelButton = Button(content, text="Cancel")


# displaying
content.grid(column=0, row=0, sticky=(N,S,E,W)) # spans everything
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
nameLabel.grid(column=3, row=0, columnspan=2, sticky=(N,W), padx=5)
nameShow.grid(column=5, row=1, columnspan=2, sticky=(N, W, S, E))
nameEntry.grid(column=5, row=0, columnspan=2, sticky=(N, E, W), padx=5, pady=5) # account for 2 colspan of namelabel
oneCheck.grid(column=0, row=1)
twoCheck.grid(column=1, row=1)
threeCheck.grid(column=2, row=1)
okButton.grid(column=5, row=2)
cancelButton.grid(column=6, row=2)

#making resize ok
root.columnconfigure(0, weight=1) # resize 1 pixel
root.rowconfigure(0, weight=1) # everytime we resize 1 pixel, resize 1 pixel

# the first three cols should be resized 3 pixels compared to the last two cols
content.columnconfigure(0, weight=3) # resize 1 pixel means resize 3 times as fast
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
# help don't see a difference between resize weight=3 and 1???

content.rowconfigure(1, weight=1)






root.mainloop()