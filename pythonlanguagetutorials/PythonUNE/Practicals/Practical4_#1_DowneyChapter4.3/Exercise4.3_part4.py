import turtle
import tkinter
import math


# 4 ------------------------------------------------------------------------
def move(t, x, y):
    """Moves a position without drawing anything.

     t: turtle object
     x: horizontal direction: if x < 0 move left, if x > 0 move right, if x == 0 do nothing
     y: vertical direction: if y < 0 move down, if y > 0 move up, if y == 0 do nothing
    """
    t.penup()
    t.goto(x, y)
    t.pendown()


def drawPolyline(t, numLineSegments, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(numLineSegments):
        t.forward(length)
        t.left(angle)


def drawPolygon(t, numSides, length):
    """ Draws numSides line segments

    tempTurtle: Turtle object
    numSides: num line segments
    length: length of each segment
    angle: degrees between segments
    """
    t.clear()
    angle = 360 / numSides
    drawPolyline(t, numSides, length, angle)


def drawArc(t, radius, angle):
    """Draws an arc with the given radius and angle.

     t: Turtle
     radius: radius
     angle: angle subtended by arc, in degrees
    """
    arcLength = 2 * math.pi * radius * abs(angle) / 360
    n = int(arcLength / 4) + 1
    stepLength = arcLength / n
    stepAngle = angle / n

    # making slight left turn before starting reduces the error
    # the error caused by the linear approximation of the arc.
    t.left(stepAngle / 2)
    drawPolyline(t, n, stepLength, stepAngle)
    t.right(stepAngle / 2)

    print(checkCircumference(n, stepLength, radius))


def position(t, radius):
    # circle centered on origin
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()


def drawCircle(t, radius):
    """ Draws a cricle

    t: turtle object
    radius: radius of circle
    """
    drawArc(t, radius, 360)


# TODO FIX: they are not equal....
def checkCircumference(n, stepLen, radius):
    epsilon = 0.0000000000000000000000001
    return abs(n * stepLen - 2 * math.pi * radius) < epsilon




if __name__ == '__main__':
    t = turtle.Turtle()

    radius = 100
    t.clear()
    position(t, radius)
    drawCircle(t, radius)

    # draw arc (partial circle)
    t.clear()
    drawArc(t, 70, 45)

    turtle.mainloop()
