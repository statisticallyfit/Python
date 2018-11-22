import turtle
import tkinter


# method summary
# http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html

t = turtle.Turtle()
# -----------------------------------------------------------------------------------------------------------

def move(tempTurtle, x, y):
    tempTurtle.penup()
    tempTurtle.goto(x, y)
    tempTurtle.pendown()

# 1, 2 ------------------------------------------------------------------------

def drawSquare(tempTurtle, length):
    for i in range(4):
        tempTurtle.forward(length)
        tempTurtle.left(90)



if __name__ == "__main__":
    drawSquare(t, 170)
    move(t, -300, -200)

    drawSquare(t, 10)
    move(t, -100, 100)

    drawSquare(t, 390)
    move(t, -100, 0)

    drawSquare(t, 5)

    turtle.mainloop()


    #NOTE:  In the browser, you need to use the following rather than turtle.mainloop()
    #turtle._Screen().end()

