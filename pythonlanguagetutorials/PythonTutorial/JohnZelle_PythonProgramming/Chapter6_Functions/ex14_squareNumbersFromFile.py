

# JOB: open file, get sum of squares of numbers in file
# ----------------------------------------------------------------------------
def isInteger(val):
    """ Returns true if string val is an integer.
    Note: having floats in strings throws value error.

    Arguments:
        val = value to check if integer
    """
    try:
        maybeVal = int(val.strip())
    except (TypeError, ValueError):
        return False # just note that except was caught
    return True


# ----------------------------------------------------------------------------
def convertToInteger(val):
    """Takes string val and converts it to int, assuming from above
     that it is an integer

     val = value to be convert
    """
    return int(val.strip())

# ----------------------------------------------------------------------------
def getFileNumbers(fileName):
    """Opens a file, reads the contents, and returns the lines as ints in a list.

    Arguments:
    fileName = name of file to open
    """
    # get the file
    inputFile = open(fileName)

    numbers = []

    # convert each item to integer (if we can)
    for line in inputFile:
        if isInteger(line):
            numbers.append(convertToInteger(line)) # add it to list
    inputFile.close()

    return numbers


# ----------------------------------------------------------------------------

def sumOfSquares(numbers):
    """Calculates the sum of the squares of numbers in the list numbers"""
    total = 0

    for num in numbers:
        total += num ** 2

    return total





if __name__ == "__main__":
    listOfNumbers = getFileNumbers("numbers.txt")
    print(sumOfSquares(listOfNumbers))