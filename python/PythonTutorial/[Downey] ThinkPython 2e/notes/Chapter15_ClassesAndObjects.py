

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

def printPoint(p):
    print("({0:.0f}, {1:.0f})".format(p.x, p.y))


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, left corner.
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


if __name__ == "__main__":
    point = Point()
    point.x = 1
    point.y = 2
    point.z = 3 # not conceptually correct
    print("x = {0}, y = {1}, z = {2}".format(point.x, point.y, point.z))

    box = Rectangle()
    # printRect(box) # has no attribues at this point
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    printRect(box)

    printPoint(findCenter(box))

    # objects are mutable
    box.width += 50
    box.height += 100

    printPoint(findCenter(box))

    box.width = 150
    box.height = 300
    printRect(box)
    print("growing: ")
    growRectangle(box, 50, 100)
    printRect(box)

    print("changing center: ")
    moveRectange(box, 1, 3)
    printRect(box)
    printPoint(findCenter(box))



    ## NOTE: copying is alternative to aliasing:
    p1 = Point()
    p1.x = 3
    p1.y = 4

    print("\n\n")

    import copy
    p2 = copy.copy(p1)
    printPoint(p1)
    printPoint(p2)
    # note: for objects, the default behavior of == is the same as 'is' = tests if they are same object.
    assert not p1 is p2
    assert not p1 == p2

    box2 = copy.copy(box)
    assert not box2 is box
    assert box2.corner is box.corner # TRue # shallow copy was made, copies objects
    # and references it contains but not embedded object.
    # So in object diagram, both box and box2 are pointing to the same point
    box2.corner.x = 23
    box2.corner.y = 24
    assert box.corner.x == 23 and box.corner.y == 24

    # this is a recursive deep copy
    box3 = copy.deepcopy(box)
    assert not box3 is box
    assert not box3.corner is box.corner # they are separate objects.

    rect2 = moveNewRectange(box, 1, 4)
    print("\nPrinting rectangles after move (deepcopy):")
    printRect(rect2)
    printRect(box)


    print(hasattr(point, 'x'))
    print(hasattr(point, 'y'))
    print(hasattr(point, 'z'))
    print(hasattr(point, 'a'))
    # OR
    try:
        x = point.x
    except AttributeError:
        x = 0
    print(x)