

# question 1

def rightJustify(aString):
    numSpaces = 80 - len(aString)
    result = aString

    # if numSpaces is 0 or negative, we don't add any space (automatic range behavior)
    for s in range(numSpaces): # 0 ... numspace-1
        result = " " + result

    print(result)


rightJustify("hi there how are youhi there how are youhi there how are youhi there how are you__")





# question 2
def drawGrid(width, height):
    """ Draw a grid with given height and width.

     width: grid width
     height: grid height
    """
    topBottom = "+" + ("-" * width) + "+"
    inside = "|" + (" " * width) + "|"

    print(topBottom)
    for i in range(height):
        print(inside)
    print(topBottom)


drawGrid(3, 4)




def solutionDrawGrid(width, height):
    # end line to display at top and bottom
    endLine = "+"
    # internal line to display for inside of grid
    internalLine = "|"

    # ste up endline and internal line
    for i in range(width):
        endLine += "-"
        internalLine += " "
    endLine += "+"
    internalLine += "|"

    # printout
    print(endLine)
    for i in range(height):
        print(internalLine)
    print(endLine)

solutionDrawGrid(3, 4)


# question 3 - look in folder in my computer



# question 4 - factorial with while loop
def factorial(n):
    if(n < 0):
        print("Factorial not defined for negative numbers")
        return
    if not isinstance(n, int):
        print("Factorial not defined for float numbers")
        return

    nTemp = n
    fact = 1

    while nTemp > 0:
        fact *= nTemp
        nTemp -= 1
    return fact

print(factorial(5))
print(factorial(4))
print(factorial(1))
print(factorial(0))
print(factorial(-10))
print(factorial(9))






# question 5 duplicates in list identifier
def hasDuplicates(lst):
    """ Checks if a list has duplicates
    lst: list to check
    """
    for elem in lst:
        if lst.count(elem) > 1:
            return True
    return False


def solutionHasDuplicates(lst):
    seen = []
    for item in lst:
        if item in seen: # if seen it, must be duplicate
            return True
        seen.append(item)

    return False # made it through list; mustn't be duplicates

assert solutionHasDuplicates([1,2,2,2,3,5,5,3,3,1,1,6]) == hasDuplicates([1,2,2,2,3,5,5,3,3,1,1,6]) == True
assert solutionHasDuplicates([1,2,3,6,4,-6]) == hasDuplicates([1,2,3,6,4,-6]) == False