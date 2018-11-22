from tkinter import *
from tkinter import ttk  # allows more modern interfaces

def calculate(*args):
    try:
        value = float(fahrenheit.get())
        celsius.set(round((value - 32) * (5/9), 5))
    except ValueError: # if couldn't convert to float then...
        pass


# note: HIERARCHY: root -> frame -> widgets. And always pass frame as parent to widgets.


#  getting a window
root = Tk()
root.title('Fahrenheit to Celsius')


# creating frame, not told it yet to display in the window
frame = ttk.Frame(root, padding ='3 3 12 12')
# telling it to display the frame
frame.grid(column=0, row=0, sticky=(N, W, E, S)) # not visible
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1) # these make it look better when adding to frame

# creating some variables, can link widgets to screen
fahrenheit = StringVar() # for inputting
celsius = StringVar() # for setting

# creating the fahrenheit input text box, parent is the frame
# linking the variable to the entry box when assigning textvariable
fEntry = ttk.Entry(frame, width=7, textvariable=fahrenheit)
# say where to display it in the frame
fEntry.grid(column=2, row=1, sticky=(W, E)) # sticky means: upon resizing, we want it to stick to the left and right

#print(fahrenheit.get())

# making the label celsius, belong to frame by giving frame arg.
cLabel = ttk.Label(frame, textvariable=celsius)
# telling it to display
cLabel.grid(column=2, row=2, sticky=(W, E))

goButton = ttk.Button(frame, text='Go', command=calculate) # the function
goButton.grid(column=3, row=3, sticky=W) # telling it to display | setting position to the right and below of the other things

fLabel = ttk.Label(frame, text='degrees F')
fLabel.grid(column=3, row=1, sticky=W) # above the Go button, same column, same sticky

dLabel = ttk.Label(frame, text='degrees C')
dLabel.grid(column=3, row=2, sticky=W)

eLabel = ttk.Label(frame, text='is equivalent to')
eLabel.grid(column=1, row=2, sticky=E)

# NOTE: Label and Entry have textvariable property when you want to apply a variable
# NOTE but use the text property when just placing text that is not a variable.

#fahrenheit.set(71)

# adding padding around everything
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5) # padx: puts space between rows, pady: space between columns.

fEntry.focus() #makes the cursor go to the fahrenheit text box
root.bind('<Return>', calculate) # makes enter activate the Go button
# # (the window is the root and inside it we put the frame)

root.mainloop()







# --------------------------------
# seeing the configure buttons

rootForButton = Tk()
b = ttk.Button(rootForButton, text="Hi, I'm a button")
b.grid(column=1, row=1)

print(b.configure()) # everything we can do with it
b.configure(text="Bye") # can change text with configure
print("Info: ", b.configure("text")) # getting information)


rootForButton.mainloop()
