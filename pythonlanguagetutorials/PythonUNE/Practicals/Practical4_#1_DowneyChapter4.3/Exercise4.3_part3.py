import turtle
import tkinter

t = turtle.Turtle()

# 3 ------------------------------------------------------------------------

def drawPolygon(tempTurtle, length, numSides):
    """ Draws numSides line segments

    tempTurtle: Turtle object
    numSides: num line segments
    length: length of each segment
    angle: degrees between segments
    """
    tempTurtle.clear()

    angle = 360 / numSides
    for i in range(numSides):
        tempTurtle.forward(length)
        tempTurtle.left(angle)

# draw square
drawPolygon(t, 40, 4)

# draw pentagon
drawPolygon(t, 100, 5)

# draw hexagon
drawPolygon(t, 30, 6)

# draw heptagon
drawPolygon(t, 40, 7)

# draw octagon
drawPolygon(t, 50, 8)

# draw nonagon
drawPolygon(t, 50, 9)

# draw decagon
drawPolygon(t, 50, 10)




# wait for user to close window
turtle.mainloop()