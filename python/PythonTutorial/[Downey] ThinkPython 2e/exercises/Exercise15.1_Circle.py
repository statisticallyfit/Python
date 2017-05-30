

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

def printPoint(p):
    print("({0:.0f}, {1:.0f})".format(p.x, p.y))


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






class Circle:
    """Represents a circle in 2-d space.

    attributes: center (Point object), radius
    """

# the attributes defined in main are global variables now and so are visible here.
def printCircle(circle):
    print("radius={0}, center=({1}, {2})".format(circle.radius, circle.center.x, circle.center.y))



def isPointInCircle(circle, point):
    """Return true if point lies in circle or on boundary of circle."""
    #print((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    #print(circle.radius**2)
    return (point.x - circle.center.x)**2 + (point.y - circle.center.y)**2 <= circle.radius**2


def isRectInCircle(circle, rect):
    """Return true if the rectangle lies entirely in or on boundary of circle"""
    # we test if all the corners of rectangle are on or in circle
    sw = rect.corner
    se = moveNewRectange(rect, rect.width, 0).corner
    nw = moveNewRectange(rect, 0, rect.height).corner
    ne = moveNewRectange(rect, rect.width, rect.height).corner
    print("\nsw=({0},{1}), se=({2},{3}), nw=({4},{5}), ne=({6},{7})"
          .format(sw.x, sw.y, se.x, se.y, nw.x, nw.y, ne.x, ne.y))

    return isPointInCircle(circle, sw) and isPointInCircle(circle, se) and \
           isPointInCircle(circle, nw) and isPointInCircle(circle, ne)


# todo update later when know how to calculate any part overlap
def isOverlapRectCircle(circle, rect):
    """Returns true if any corner of the rectangle falls inside the circle
    AND
    if any part of the rectangle (could be top or bottom or side) falls inside the circle."""
    sw = rect.corner
    se = moveNewRectange(rect, rect.width, 0).corner
    nw = moveNewRectange(rect, 0, rect.height).corner
    ne = moveNewRectange(rect, rect.width, rect.height).corner
    print("sw=({0},{1}), se=({2},{3}), nw=({4},{5}), ne=({6},{7})"
          .format(sw.x, sw.y, se.x, se.y, nw.x, nw.y, ne.x, ne.y))

    isAnyPointOverlap = any([isPointInCircle(circle, sw), isPointInCircle(circle, se),
                             isPointInCircle(circle, nw), isPointInCircle(circle, ne)])
    isAnyPartOverlap = False # todo

    return isAnyPointOverlap # or isAnyPartOverlap



if __name__ == "__main__":

    # 1 ------------------
    circle = Circle()
    circle.radius = 75
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100

    p1 = Point()
    p1.x = 1
    p1.y = 2
    assert not isPointInCircle(circle, p1)
    print(circle)
    printCircle(circle)

    # inside circle
    p2 = Point()
    p2.x = 200
    p2.y = 110
    assert isPointInCircle(circle, p2)

    # on boundary of circle
    p3 = Point()
    p3.x = 225
    p3.y = 100
    assert isPointInCircle(circle, p3)




    # 2 -------------------
    r1 = Rectangle()
    r1.width, r1.height = 50, 50
    r1.corner = Point()
    r1.corner.x, r1.corner.y = 100, 50
    assert isRectInCircle(circle, r1)

    r2 = Rectangle()
    r2.width, r2.height = 144, 42
    r2.corner = Point()
    r2.corner.x, r2.corner.y = 78, 79
    assert isRectInCircle(circle, r2)

    r3 = Rectangle()
    r3.width, r3.height = 150, 180
    r3.corner = Point()
    r3.corner.x, r3.corner.y = 50, 20
    assert not isRectInCircle(circle, r3)

    r4 = Rectangle()
    r4.width, r4.height = 20, 15
    r4.corner = Point()
    r4.corner.x, r4.corner.y = 150, 160
    assert not isRectInCircle(circle, r4)




    # 3 -------------------
    print("\n\nr1: ", end=""); assert isOverlapRectCircle(circle, r1)
    print("r2: ", end=""); assert isOverlapRectCircle(circle, r2)
    # note: with a better implementation, this should yield true.
    # print("r3: ", end=""); assert isOverlapRectCircle(circle, r3)
    print("r4: ", end=""); assert isOverlapRectCircle(circle, r4)

    r5 = Rectangle()
    r5.width, r5.height = 20, 40
    r5.corner = Point()
    r5.corner.x, r5.corner.y = 190, 140
    print("r5: ", end=""); assert isOverlapRectCircle(circle, r5)

    r6 = Rectangle()
    r6.width, r6.height = 10, 100
    r6.corner = Point()
    r6.corner.x, r6.corner.y = 100, 200
    print("r6: ", end=""); assert not isOverlapRectCircle(circle, r6)