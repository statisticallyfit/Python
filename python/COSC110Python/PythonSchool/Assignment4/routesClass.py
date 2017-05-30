"""
'''
GOAL / PURPOSE:

--- General description: ---
Read input from a file about routes and unhappy ratios and store them in a dictionary, then sort
them according to the happy ratios to find the number (n) of these routes that could use an extra bus.

--- Detailed description: ---
1. Read in VALID input in the format: "route, happy ratio"
2. Create a list of dictionaries with this data
3. Sort the list of dictionaries by their happy ratio
4. Input the (n) amount of routes that would benefit from the extra buses - these are the route dicts
that are at the top, sorted low to high by their happy ratio with zeroes at the bottom.
5. Print the list of routes that could most use an extra bus, because happy ratios are lowest.
'''


import busstop
import testRoute



# ----------------------------------------- Part 1: input validation -----------------------------------------

class RouteData:
    '''A class that represents a list of dictionaries, where each dict has 2 keys:
    happyRatio and routeNumber.'''
    def __init__(self, fileName):
        self.fileName = fileName

    #def readRouteData(self):

# global variable: stores a record of inputted routes to handle double route inputs (invalid input)
ROUTE_RECORD = None


def isValidPosInt(stringValue):
    '''Returns true if the string input can be turned into an int AND is
    greater than zero (strictly).
    Argument:
        stringValue - the user input.
    Returns:
        boolean - true or false
    '''
    try:
        maybeInt = int(stringValue)
    except (TypeError, ValueError):
        return False
    else: # else if it got converted to int, check if positive
        return maybeInt > 0




def isValidRoute(routeStr):
    '''Tests if the routeStr is a valid route number (if it is greater than 0 and
    is a unique route not mentioned before).

    routeStr -- the string route value (stripped of front/end whitespace)
    return: true if valid route, false otherwise
    '''
    global ROUTE_RECORD

    if not isinstance(routeStr, str):
        return False

    # check that ratio has no gaps after it: (none will be before since we stripped the inputLine before
    # # passing into this function.)
    if not len(routeStr) == len(routeStr.strip()):
        return False


    if isValidPosInt(routeStr):
        route = int(routeStr)
        if isUniqueRoute(route):
            if ROUTE_RECORD is None:
                ROUTE_RECORD = []
            else:
                ROUTE_RECORD.append(route) # now recorded in list
            return True
        return False  # not valid by uniqueness

    return False # not valid by pos/int



def isValidRatio(ratioStr):
    '''Returns true if the given string ratio is a float, and ends in no more than 2 decimal places.

    ratioStr -- the string ratio
    return: true if ratio is valid, false if not.
    '''
    if not isinstance(ratioStr, str):
        return False

    # check that ratio has no gaps before it:
    if not len(ratioStr) == len(ratioStr.strip()):
        return False

    # does ratioStr have the correct type and value?
    try:
        float(ratioStr) # note: ratio must be convertible to float.
    except ValueError: # note: no typeerror anticipated here because type ratioStr == str
        return False

    # does ratioStr end with two decimal places?
    firstSecond = ratioStr.split(".")

    # check we only have at most 1 decimal point and if so then check no more than 2 decimal places.
    atMostOneDecimal = len(firstSecond) == 1 and not len(firstSecond[0]) == 0
    noMoreThanTwoDecimals = len(firstSecond) == 2 and len(firstSecond[1]) == 2
    return atMostOneDecimal and noMoreThanTwoDecimals

'''
    # check we only have at most 1 decimal point and if so then check no more than 2 decimal places.
    return len(firstSecond) == 1 or (len(firstSecond) == 2 and len(firstSecond[1]) <= 2)
'''


def isValidInput(inputLine):
    '''Returns true if the input line has two items only that are separated by a comma.
    The first item should be a valid route number and the second a valid ratio.

    inputLine --- a single string line
    return: true if input line string is valid, false if not.
    '''
    if not isinstance(inputLine, str):
        return False

    routeRatio = inputLine.split(",") # need above check so we are sure we are working on a string.

    if len(routeRatio) == 2:
        # check if both the route number and ratio are valid
        routeRatio[0]
        #routeStr = routeRatio[0]
        #ratioStr = routeRatio[1]
        return isValidRoute(routeRatio[0]) and isValidRatio(routeRatio[1])

    return False




def isUniqueRoute(givenRoute, prevRoutes=ROUTE_RECORD):
    '''Returns true if the int route type argument is not in the previous
    list of routes, else it returns false.

    routeFloat -- the route as int type
    return: true if route int is unique, false if not.
    '''
    if not isinstance(givenRoute, int):
        return False

    if prevRoutes is None:
        return True

    # if it goes through all routes without returning false, then must return true
    # - it won't be in the list.
    for route in prevRoutes:
        if route == givenRoute:
            return False
    return True







# ------------------------------------------- Part 2: Reading Input -------------------------------------------


def readRouteData(fileName):
    '''Takes a file name, reads its lines and returns a list of dictionaries,
    where each dictionary has keys routeNumber and happyRatio.
    If the data input is not valid, throw an exception.

    fileName --- string name of file
    return: exception if invalid input or the dictionary if valid input..
    '''
    if not isinstance(fileName, str):
        raise TypeError("Error: Filename type was invalid.") # note: raise, don't return error!

    # trying to open the file
    try:
        fileIn = open(fileName, "r")
    except IOError:
        raise IOError("Error: Something went wrong opening the file.")

    # making the list to hold dictionaries
    listOfDicts = []

    # if file is valid, we read the input
    for aLine in fileIn:
        line = aLine.strip() # removing whitespace - that doesn't count as error.
        if not isValidInput(line):
            raise ValueError("Error reading data."
                             "\nPlease ensure each line of routes.txt contains a route number, "
                             "followed by a comma, followed by a happy ratio "
                             "\nand that no route is repeated "
                             "throughout the file.")
        listOfDicts.append(makeDict(line))

    fileIn.close()

    return listOfDicts



def makeDict(routeRatioLineStr):
    '''Returns a dictionary with keys routeNumber and happyRatio and values corresponding
    to these.  No need to throw exception because the input is valid if it made it this far.

    routeRatioLineStr --- the valid file input line.
    return: dictionary
    '''
    # input is valid if it succeeded this far so we can split it directly into the tuple.
    routeStr, ratioStr = routeRatioLineStr.split(",")
    return {"routeNumber" : int(routeStr), "happyRatio" : float(ratioStr)}




# ------------------------------------ Part 3: Sorting the Data Structure ------------------------------------


def sortRouteData(routeData):
    '''Sorts the list of dictionaries by the happyRatio key from lowest to highest, although all zero
    ratios go last because that is where the amount of unhappy people is zero. Uses the insertion sort algorithm.

    routeData: list of dictionaries with two keys - happyRatio and routeNumber
    return: sorted newRouteData by happyRatio as described and zero ratios at the end.
    '''
    # separate dicts with zero/non-zero happy ratios and put them in new dict in their exact order.
    newRouteData = []
    zeroRouteData = []
    for dct in routeData:
        if dct["happyRatio"] != 0:
            newRouteData.append(dct)
        else:
            zeroRouteData.append(dct) # so that we don't have to go over the list again and collect the zeroes.

    # the insertion sort
    for i in range(1, len(newRouteData)): # n - 1 passes
        j = i
        while j > 0 and newRouteData[j]['happyRatio'] < newRouteData[j - 1]['happyRatio']:
            swap(newRouteData, j - 1, j)
            j = j - 1

    # Now just add the zero-dicts from the old list onto the new list (it doesn't matter how they are ordered):
    newRouteData.extend(zeroRouteData)

    return newRouteData



def swap(dct, x, y):
    '''Swaps the dictionary values so that at index x we get index y's value
     and at index y we get index x's value, assuming we swap at the happyRatio key.
     dct -- dictionary whose values are to be swapped.
     '''
    dct[x]['happyRatio'], dct[y]['happyRatio'] = dct[y]['happyRatio'], dct[x]['happyRatio']





# -------------------------------------------- Part 4: Working with N: ---------------------------------------------
def isValidN(nStr, numBuses):
    '''Returns true if the n satisfies: 0 <= n <= numBuses or false if not,
    where n = int(nStr).

    nStr --- number of routes that would benefit from extra buses, as string parameter.
    numBuses -- number of buses = number of routes
    '''
    try:
        int(nStr)
    except (TypeError, ValueError):
        return False
    # else
    return 0 <= int(nStr) <= numBuses


def getNRoutes(n, routeData):
    '''Returns the n route numbers in a list that would benefit from having extra buses.

    n --- the integer number of routes that would benefit from extra buses.
    routeData --- the list of dictionaries
    return: list that holds n route numbers.
    '''
    busLackingRoutes = []
    for i in range(n):
        busLackingRoutes.append(routeData[i]['routeNumber'])
    return busLackingRoutes



def showRoutes(routes):
    '''Returns the list of routes as a string.

    routes -- list of integer routes
    return: None
    '''
    # step 1: show routes as ordinary list but take off the []
    routeStr = str(routes)[1:-1]

    # step 2: split the routes at the comma and join them with first tab then newline, including tab before first.
    routesNice = '\t ' + '\n\t'.join(routeStr.split(","))

    # must do this check otherwise we return '\t' if routesNice == ''
    toShow =  "" if len(routesNice) == 0 else routesNice
    print(toShow)



'''
if __name__ == "__main__":
    testRoute.testValidInput()
    testRoute.testValidRatio()
    testRoute.testValidRoute()
    testRoute.testUniqueRoute()
'''


if __name__ == "__main__":


    data = []
    try:
        data = readRouteData("routes_sample_2.txt")
    except BaseException as err: #(TypeError, IOError, ValueError)
        print(str(err))
    else:
        # sort the data
        orderedData = sortRouteData(data)

        # Ask the user for n :
        n = input("How many routes do you want to benefit from extra buses?: ")
        while not isValidN(n, len(orderedData)): # remember: numBuses = numRoutes because there's 1 bus per route.
            print("Invalid value. Please enter a non-negative integer. Make sure input is <= number of buses.")
            n = input("How many routes do you want to benefit from extra buses?: ")

        # output the routes needing extra buses:
        n = int(n)
        print("\nYou should add buses for the following routes: ")
        routeList = getNRoutes(n, orderedData)
        showRoutes(routeList)
'''
if __name__ == "__main__":

    data = []
    try:
        data = readRouteData("routes_sample_2.txt")
    except BaseException as err: #(TypeError, IOError, ValueError)
        print(str(err))
    else:
        # sort the data
        orderedData = sortRouteData(data)

        # Ask the user for n :
        n = input("How many routes do you want to benefit from extra buses?: ")
        while not isValidN(n, len(orderedData)): # remember: numBuses = numRoutes because there's 1 bus per route.
            print("Invalid value. Please enter a non-negative integer. Make sure input is <= number of buses.")
            n = input("How many routes do you want to benefit from extra buses?: ")

        # output the routes needing extra buses:
        n = int(n)
        print("\nYou should add buses for the following routes: ")
        routeList = getNRoutes(n, orderedData)
        showRoutes(routeList)
'''
"""