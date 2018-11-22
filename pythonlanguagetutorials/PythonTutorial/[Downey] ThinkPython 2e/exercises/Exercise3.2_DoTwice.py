from __future__ import print_function, division





def doTwice(f):
    f()
    f()


def printHoney():
    print("honey")

# --------------------------------

def doTwiceArg(f, value):
    f(value)
    f(value)

def cubeIt(num):
    print(num ** 3)

# --------------------------------

def doFourArg(f, value):
    doTwiceArg(f, value)
    doTwiceArg(f, value)


# leave off parantheses on function object else TypeError: nonetype object is not callable
doTwice(printHoney)
doTwiceArg(cubeIt, 5)
print("\nFour this time: ")
doFourArg(cubeIt, 5)



# ------------------------------------------------------------------------------------


# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

'''def do_twice(f):
    f()
    f()
'''

'''
def doFour(f):
    doTwice(f)
    doTwice(f)

def printBeam():
    print('+ - - - -', end=' ')

def printPost():
    print('|        ', end=' ')

def printBeams():
    doTwice(printBeam); print('+')

def printPosts():
    doTwice(printPost); print('|')

def printRow():
    printBeams()
    doFour(printPosts)

def printGrid():
    doTwice(printRow)
    printBeams()


print("\n\n")
printGrid()
'''


def doFour(f):
    doTwice(f)
    doTwice(f)

def printBeam():
    print('+ - - - -', end=' ')

def printBeams():
    doTwice(printBeam); print("+")

def printPost():
    print('|        ', end=' ')

def printPosts():
    doTwice(printPost); print("|")

def printRow():
    printBeams()
    doFour(printPosts)

def printGrid2by2():
    doTwice(printRow)
    printBeams()



print("\n\nGRID 2x2: ")
printGrid2by2()



# -------------------------------------------------------------------------------------------------------------------
# NOTE: press Alt+D when disabling preview window for refactoring

# here is a less-straightforward solution to the
# four-by-four grid

def oneFourOne(f, g, h):
    f()
    doFour(g)
    h()

def printPlus():
    print('+', end=' ')

def printDash():
    print('-', end=' ')

def printBar():
    print('|', end=' ')

def printSpace():
    print(' ', end=' ')

def printEnd():
    print()

def nothing():
    "do nothing"

def print1beam():
    oneFourOne(nothing, printDash, printPlus)

def print1post():
    oneFourOne(nothing, printSpace, printBar)

def print4beams():
    oneFourOne(printPlus, print1beam, printEnd)

def print4posts():
    oneFourOne(printBar, print1post, printEnd)

def printRowForGrid4by4():
    oneFourOne(nothing, print4posts, print4beams)

def printGrid4by4():
    oneFourOne(print4beams, printRowForGrid4by4, nothing)

print("\n\nGRID 4x4: ")
printGrid4by4()