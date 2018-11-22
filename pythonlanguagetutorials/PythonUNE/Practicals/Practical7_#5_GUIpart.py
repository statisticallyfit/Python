# NOTE:: did all this by seeing the answers directly so mull this over and be capable
# note of doing it alone after exam over.



from tkinter import *
from tkinter import ttk

# setting up window
root = Tk()
root.title("Chatter")


# Setting up required variables
usernames = ["alice", "bob", "charlie", "dianne", "ethan", "freda", "gary", "helen"]
entryVariable = StringVar() # string var 1 is just an empty variable string
choicesListBox = StringVar(value = usernames) # string var 2 is a string var with list of names # note: would get this to be a list of logged-in users.



# Setting up widgets
contentFrame = Frame(root, relief="groove")
outputText = Text(contentFrame)

chatScroll = Scrollbar(contentFrame, orient=VERTICAL, command=outputText.yview)
outputText['yscrollcommand'] = chatScroll.set # making command work

label = Label(contentFrame, text="bob: ") # note:  you would set this when user logs in.

entry = Entry(contentFrame, textvariable=entryVariable) # setting it to empty variable for now.

button = Button(contentFrame, text="Send")

users = Listbox(contentFrame, listvariable=choicesListBox)

usersScroll = Scrollbar(contentFrame, orient=VERTICAL, command=users.yview)
users['yscrollcommand'] = usersScroll.set




# Place widgets
# note: when resizing, sticky means resize in that direction as well. So if no W
# note - then upon resizing, the widget doesn't resize in that direction.
contentFrame.grid(sticky=(N, W, S, E)) # means frame fills up all corners
outputText.grid(row=1, column=1, columnspan=2, sticky=(N, W, S, E)) # text fills up all corners (until col 2 beacuse colspan=2)
chatScroll.grid(row=1, column=3, sticky=(N, S, W)) # help: difference in putting E as well?
label.grid(row=2, column=1, sticky=E)
entry.grid(row=2, column=2, sticky=(E, W)) # means stick to left and right corners (no need for N, S since already at top/bottom)
button.grid(row=2, column=3, columnspan=2, sticky=W, padx=(5,0)) # means pad 5 just on left, 0 padding on the right.
users.grid(row=1, column=4, sticky=(N, S, E, W), padx=(5,0))
usersScroll.grid(row=1, column=5, sticky=(N, S, W))





# Configure resizing
# note: need to do this base root window resizing before all others
root.columnconfigure(0, weight=1) # this enables resizing along cols
root.rowconfigure(0, weight=1)
#root.rowconfigure(1, weight=1) # todo this makes no difference


contentFrame.columnconfigure(1, weight=1)
contentFrame.columnconfigure(2, weight=3)
#contentFrame.columnconfigure(3, weight=1) # help: why we would want separation between listbox and textbox I don't know??
contentFrame.columnconfigure(4, weight=3) # note: even at 100, still not fast enough to resize with window
#contentFrame.columnconfigure(5, weight=1) # help: why we would want separation between listbox and outer edge I don't know!

contentFrame.rowconfigure(1, weight=1)



def insertLine(textVar, user, quote):
    textVar.insert("end", "{0}: {1}\n".format(user, quote))


# Adding conversation to textbox
insertLine(outputText, "gary", "did you see the latest:")
insertLine(outputText, "gary", "http://www.dailydot.com/politics/encryption-crypto-wars-backdoors-timeline-security-privacy/")
insertLine(outputText, "helen", "Not yet - what's it about")
insertLine(outputText, "gary", "the crypto war")
insertLine(outputText, "bob", "I saw that yesterday")
insertLine(outputText, "helen", "I'll go look at it now")
insertLine(outputText, "bob", "It's become more of a political issue than it really should be")
insertLine(outputText, "bob", "I mean it's all well known now, there's no way to really stop it")
insertLine(outputText, "helen", "Interesting")
insertLine(outputText, "helen", "Yes, making encryption illegal would mean only outlaws had encryption")
insertLine(outputText, "bob", "Exactly!")
insertLine(outputText, "gary", "hopefully they'll realise that")
insertLine(outputText, "alice", "Hi everybody!")
insertLine(outputText, "helen", "Hi alice!")
insertLine(outputText, "bob", "Hey")
insertLine(outputText, "alice", "What's happening?")
insertLine(outputText, "helen", "Nothing much")
insertLine(outputText, "charlie", "I just got here too")
insertLine(outputText, "bob", "We've been discussing the latest war on encryption")
insertLine(outputText, "alice", "I really don't understand it")
insertLine(outputText, "alice", "I mean, without strong encryption, nobody has privacy")
insertLine(outputText, "gary", "I certainly wouldn't trust Internet banking without it")
insertLine(outputText, "charlie", "you couldn't!")

entryVariable.set("It'd basically be making maths illegal.")


# stop output text from being editable
outputText["state"] = "disabled"


root.mainloop()


#print("entry var: ", entryVariable.get())
