from tkinter import *
from tkinter import ttk

import numpy as np

'''
GOAL OF THIS FILE:

Create a cleanliness rater window that contains five buttons. Allow the user to click on any
of the buttons. As a result, the average rating should appear at the bottom of the window
(mandatory feature) as well as the total number of times the user has clicked any button
(optional feature).
Author: Ana-Maria Vintila.
Date: 5/19/2017
'''


# STATE:

# make an array of partitions so that 1 to 5 take up 50 values (never changes in life of program)
partitions = np.linspace(1, 5, 50)

# make a color list (never changes in life of program). This has same length 50



# Functions

#def updateBackground():

def calcAverage(averageVar, averageTextVar, summingVar, n, counterVar):
    '''
    A function that updates the sum, count and thus the average rating.

    :param averageVar: the DoubleVar of current average rating.
    :param averageTextVar: the StringVar that reports the average rating onscreen.
    :param summingVar: the IntVar total button value sum.
    :param n: the int amount by which to increase the summingVariable when updating the averageVar
    :param counterVar: the IntVar of total counts the buttons were clicked, or how many times average
    was updated.

    :return: None
    '''
    summingVar.set(summingVar.get() + n) # increasing total rating sum by incrSumBy
    counterVar.set(counterVar.get() + 1) # one item has been included
    averageVar.set(summingVar.get() / counterVar.get()) # updating average
    averageTextVar.set("This location has an average cleanliness rating of: {0:.2f} out of {1} ratings."
                       .format(round(averageVar.get(), 2), counterVar.get()))




if __name__ == "__main__":

    # Setting Up Window --------------------------------------------------------------------------
    root = Tk()
    root.title("Cleanliness Rater")


    # Setting Up Variables -----------------------------------------------------------------------
    avgTextVar = StringVar(value="This location has not yet been rated.") # will be updated
    sumVar = IntVar() # total sum of click values
    countVar = IntVar() # number of times clicked so far
    avgVar = DoubleVar() # the running average (double)


    # Setting Up Widgets -------------------------------------------------------------------------
    frame = Frame(root, width=600, height=400)

    instructLabel = Label(frame, text="Rate the cleanliness of this location: ",
                          font=("Verdana", 17, "bold")) # static, doesn't get changed
    avgLabel = Label(frame, textvariable=avgTextVar,
                     font=("Verdana", 10)) # gets changed when we click the buttons (updating average variable)

    smileyLabel = Label(frame, text=":-)", font=("Verdana", 18, "bold")) # doesn't get changed
    frowneyLabel = Label(frame, text=":-(", font=("Verdana", 18, "bold")) # doesn't get changed


    button1 = Button(frame, width=8, height=5, text="1",
                     font=("Verdana", 20, "bold"), bg="white", fg="red3",
                     command = lambda: calcAverage(avgVar, avgTextVar, sumVar, 1, countVar))

    button2 = Button(frame, width=8, height=5, text="2",
                     font=("Verdana", 20, "bold"), bg="white", fg="orange",
                     command = lambda: calcAverage(avgVar, avgTextVar, sumVar, 2, countVar))

    button3 = Button(frame, width=8, height=5, text="3",
                     font=("Verdana", 20, "bold"), bg="white", fg="olivedrab3",
                     command = lambda: calcAverage(avgVar, avgTextVar, sumVar, 3, countVar))

    button4 = Button(frame, width=8, height=5, text="4",
                     font=("Verdana", 20, "bold"), bg="white", fg="seagreen",
                     command = lambda: calcAverage(avgVar, avgTextVar, sumVar, 4, countVar))

    button5 = Button(frame, width=8, height=5, text="5",
                     font=("Verdana", 20, "bold"), bg="white", fg="dodgerblue",
                     command = lambda: calcAverage(avgVar, avgTextVar, sumVar, 5, countVar))



    # Placing Widgets --------------------------------------------------------------------------
    frame.grid(row=0, column=0, padx=40, pady=60)

    # note: either sticky of N, S, W, E or just W, E will work fine.
    button1.grid(row=2, column=2, sticky=(W, E), padx=3)
    button2.grid(row=2, column=3, sticky=(W, E), padx=3)
    button3.grid(row=2, column=4, sticky=(W, E), padx=3)
    button4.grid(row=2, column=5, sticky=(W, E), padx=3)
    button5.grid(row=2, column=6, sticky=(W, E), padx=3)

    # note padding x of (0, 10) meaning there is 10+3 padding between frowney and button 1
    frowneyLabel.grid(row=2, column=1, sticky=(W, E), padx=(0, 10))
    # note padding x of (10, 0) meaning there is 10+3 padding between smiley and button 5
    smileyLabel.grid(row=2, column=7, sticky=(W, E), padx=(10, 0))

    # note even though avLabel changes width, its colspan is 5 so when it changes length, it doesn't make buttons resize.
    # note if the avgLabel is 2 then it makes the 1 and 2 buttons resize! Avoid this colspan=2 at all costs. Make it 5 for consistency and to place it in the middle.
    # If the colspan of avgLabel is 1 then the smiley/frowney faces get obscured when average label value changes.
    instructLabel.grid(row=1, column=2, columnspan=5, sticky=(N, S, E, W), pady=(0, 60))
    avgLabel.grid(row=3, column=2, columnspan=5, sticky=(N, W, S, E), pady=(40, 0))


    # Configure Resizing --------------------------------------------------------------------------
    # note: the weights here aren't that important, it is ok if they are all 1.
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)
    frame.columnconfigure(5, weight=1)
    frame.columnconfigure(6, weight=1)
    frame.columnconfigure(7, weight=1)

    frame.rowconfigure(1, weight=1)


    # Allow The User To Close The Program
    root.mainloop()