
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    assert y != 0
    return x / y



def calculateStrangeValue(x, y):
    if x < y:
        return mul(mul(x, y), add(x, y))
    elif x > y:
        return mul(div(x,y), sub(x,y))
    else:
        return 1

def isValidPositiveIntegerInput(stringValue):
    # FIXED added this check at top:
    if not isinstance(stringValue, (str, int)):
        return False

    try:
        maybeInt = int(stringValue)
    except (TypeError, ValueError):
        print("ERROR: cannot be converted to int: ", stringValue)
        return False
    else: # else if it got converted to int, check if positive
        return maybeInt > 0




if __name__ == "__main__":
    epsilon = 0.00000000000000000000000000000000000000000000000000000000000001

    firstInt = -1
    secondInt = -1

    while not isValidPositiveIntegerInput(firstInt):
        firstInt = input("Enter first positive integer: ")
    while not isValidPositiveIntegerInput(secondInt):
        secondInt = input("Enter second positive integer: ")

    firstInt = int(firstInt)
    secondInt = int(secondInt)

    print("Strange value: ", calculateStrangeValue(firstInt, secondInt))


    '''
    f, s = map(int, input("Input two nums: ").split())
    f = int(f)
    s = int(s)
    print(f, s)
        '''