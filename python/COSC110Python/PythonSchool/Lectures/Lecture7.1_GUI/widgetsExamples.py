

from tkinter import *
from tkinter import ttk
#import Image, ImageTk

root = Tk()
frame = ttk.Frame(root, width=600, height=400, padding=5)
frame.grid()


# ABOUT FRAMES

for k, v in frame.configure().items():
    print(k, v)
frame.configure(borderwidth = 5)
frame.configure(relief="solid")
# or simpler instead of using configure
frame["relief"] = "flat"
frame["relief"] = "solid"
frame["relief"] = "raised"
frame["relief"] = "sunken"
frame["relief"] = "ridge"
frame["relief"] = "groove"




# ABOUT LABELS:
label = Label(frame, text="label")
label.grid() # telling it to display (resized to be small)
label["text"] = "Hello COSC110" # configuring
variable = StringVar()
label["textvariable"] = variable # empty value, empty string
variable.set("Hello, setting a variable")
variable.set(variable.get() + "\nThis is a new line.")
label["justify"] = "left" # is by default
label["justify"] = "right"
label["justify"] = "center"


image = PhotoImage(file="tux.gif")
label["image"] = image # text has disappeared
# setting compound of the label
#label["compound"] = "text" # means just display text # help
#label["compound"] = "image" # means just display image # help error
label["compound"] = "left" # display image to left of text
label["compound"] = "right" # display image to right of text
label["compound"] = "bottom" # display image bottom of text
label["compound"] = "top" # display image top of text
label["compound"] = "center" # image with text in center
label["compound"] = "none" # default: if image, display it, if no image, then display text

label.grid_remove() # takes the label away from window (remove it from being displayed, still in memory)



# buttons
button = Button(frame, text = "Click me") # creating it
button.grid()

def click(*args):
    print("Button was clicked")

button["command"] = click # setting it to function

# help he says spacebar should activate
button["default"] = "normal" # setting button as normal
button["default"] = "active" # setting button as default (like default cancel or ok)

# programmatically invoke the method
button.invoke()

#disabling
button["state"] = "disabled"
button["state"] = "active" # help !disabled doesn't work


# help print(button.instate(["disabled"])) # checking to see if state is disabled
button["state"] = "disabled"
# help print(button.instate(["disabled"]))
button.grid_remove()





# Checkbutton
selected = StringVar()
checkbutton = Checkbutton(frame, text="Click me checkbutton", variable=selected)
checkbutton.grid()
checkbutton["onvalue"] = "selected"
checkbutton["offvalue"] = "not selected"
print(selected.get()) # key: put after mainloop

checkbutton.grid_remove()




# Radio buton
firstRadio = Radiobutton(frame, variable=selected, text="first",
                         value="first")
secondRadio = Radiobutton(frame, variable=selected, text="second",
                          value="second")
firstRadio.grid(row=1, column=1)
secondRadio.grid(row=2, column=1)
selected.set("second")
selected.set("") # setting both to blank

print(selected.get())# key: put after mainloop
firstRadio.grid_remove()
secondRadio.grid_remove()




# Entry
entry = Entry(frame, textvariable=variable) # just single line - can't display newline
entry.grid()
variable.set("Hello COSC110")

print(variable.get()) # put after mainloop

entry["state"] = "readonly"
entry["state"] = "normal"

entry["show"] = "*"
entry["show"] = "" # comes back to empty letters






# VALIDATION
def hasNoSpaces():
    return " " not in variable.get()
    # return true if space is not in there, false if it is.

def removeSpaces():
    variable.set(variable.get().replace(" ", ""))

entry["validatecommand"] = hasNoSpaces
entry["invalidcommand"] = removeSpaces # what it does if there are spaces
entry["validate"] = "key" # when it should validate - at every keystroke
# help not working

entry["validate"] = "focus" # remove spaces when clicking into the entry.
entry["validate"] = "focusin" # spaces removed only when you click on, come back when go out
entry["validate"] = "focusout" # spaces removed only when you click out of entry and come back when come in
entry["validate"] = "none"
entry.grid_remove()





# Combobox
combobox = ttk.Combobox(frame, textvariable = variable)
combobox["values"] = ("First", "Second", "Third")
combobox.grid()

print(variable.get()) #put after mainlooop
#combobox["state"] = "readonly"  #cannot type own words


# Calling this when combobox is changed
def notify(event):
    print("Selected {0}".format(variable.get()))

# whenever this event occurs, perform the notify
combobox.bind("<<ComboboxSelected>>", notify)

combobox.grid_remove()





# List of options
choices = ("First", "Second", "Third")
variable = StringVar(value = choices)

print(variable.get()) # print after loop

# no need to do ttk.Listbox since hasn't changed in a long time
listbox = Listbox(frame, listvariable = variable)
listbox.grid(column=1, row=1)
# help - can't print value after loop!

listbox["selectmode"] = "extended" # selecting multiple ones
listbox["selectmode"] = "browse" # selecting one

print(listbox.curselection()) # tells in numbers which are selected # help error


def notifyListBox(event):
    print("New selection: {0}".format(listbox.curselection()))

listbox.bind("<<ListboxSelect>>", notifyListBox)



# adding more choices
choices = []
for i in range(100):
    choices.append("Item {0}".format(i))

variable.set(value = choices)





# Creating scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
scrollbar.grid(column=2, row=1, sticky=(N, S))

# need to show change in scrollbar
listbox["yscrollcommand"] = scrollbar.set

scrollbar.grid_remove()





# Text
text = Text(frame, width=40, height=10)
text.grid(column=1, row=1)
scrollbar.grid(column=2, row=1, sticky=(N, S)) # still was in memory, telling it to reshow
scrollbar["command"] = text.yview
text['yscrollcommand'] = scrollbar.set # setting it both ways



# adding text wrapping
text['wrap'] = "none" # means you need horizontal scrollbar.
text['wrap'] = 'char' # wrap on char
text['wrap'] = 'word' # wrap on word


# changing programmatically
text.insert("end", "Hello World") # inserting at end
text.insert("1.2", "Hello World") # line 1, char 2 (overwrites or really inserts)

text.delete("1.2", "1.4") # the range
#print(text.get("1.1", "end")) # from line 1, char 1 to end
#print(text.get("1.1", "1.5"))
# help error


root.mainloop()