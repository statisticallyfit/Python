
class Rectangle:
    """Represents a rectangle.

    attributes: width, height, left bottom (southwest) corner.
    """

def printRect(rect):
    print("(w={0}, h={1}, ({2}, {3}))".format(rect.width, rect.height, rect.corner.x, rect.corner.y))


def findCenter(rect):
    """Returns a Point at center of Rectangle.

    rect: Rectangle
    return: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


def growRectangle(rect, deltaWidth, deltaHeight):
    rect.width += deltaWidth
    rect.height += deltaHeight

def moveRectange(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def moveNewRectange(rect, dx, dy):
    import copy

    newRect = copy.deepcopy(rect)
    newRect.corner.x += dx
    newRect.corner.y += dy
    return newRect





class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


def move(t, x, y):
    """Moves a position without drawing anything.

     t: turtle object
     x: horizontal direction: if x < 0 move left, if x > 0 move right, if x == 0 do nothing
     y: vertical direction: if y < 0 move down, if y > 0 move up, if y == 0 do nothing
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

def drawRect(rect, t):
    # move to location left corner
    move(t, rect.corner.x, rect.corner.y)

    for i in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)



if __name__ == "__main__":
    import turtle

    tut = turtle.Turtle()
    rect = Rectangle()
    rect.width = 100
    rect.height = 140
    rect.corner = Point()
    rect.corner.x, rect.corner.y = 5, 5


    drawRect(rect, tut)

    turtle.mainloop()