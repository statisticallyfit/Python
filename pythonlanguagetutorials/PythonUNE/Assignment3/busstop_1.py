## NOTE: Comment at top needed to describe purpose of file.
'''
The purpose of this file is to get data of people waiting at the bus stop,
take as many as seats will allow, and calculate the ratio of unhappy to happy
customers at the end of the route.
Input: number of stops, number of people waiting at the stop, and route number
Output: ratio of happy to unhappy customers to 2 decimal points.
'''




MAX_SEATS = 50
seatsLeftCount = MAX_SEATS
onBusCount = 0
happyCustomers = 0
unhappyCustomers = 0


def getOnBus(waiting):
    '''Updates the onBusCount, seatsLeftCount, happyCustomers, and unhappyCustomers
     by the number of passengers waiting when the bus arrives at the stop.
     Argument:
        waiting - number of passengers waiting at the stop.
     Return:
         None
    '''
    global seatsLeftCount, onBusCount
    global happyCustomers, unhappyCustomers

    if waiting < seatsLeftCount:
        onBusCount += waiting # allow all the waiting ones inside
        seatsLeftCount -= waiting # seatsleft decreases by the ones added
        happyCustomers += waiting # they are all happy since all fit inside
    elif waiting > seatsLeftCount:
        unhappyCustomers += waiting - seatsLeftCount # unhappy are the ones not able to fit inside

        onBusCount += seatsLeftCount # accept all that the bus can fit
        happyCustomers += seatsLeftCount # happy are those that fit (equal to amount of seats left)
        seatsLeftCount = 0 # seats left is none
    else: #if waiting == seatsLeftCount
        onBusCount += seatsLeftCount # perfect fit
        happyCustomers += seatsLeftCount # happy are the ones that are let in; none unhappy since all are allowed in.
        seatsLeftCount = 0  # but no more seats left.


def getOffBus(leaving):
    '''Given the number leaving is not greater than number currently on bus, we
     decrease the number on the bus and increase seats left by the number who are leaving.
     Argument:
         leaving - number of passengers leaving the bus.
     Return:
         None
    '''
    global seatsLeftCount, onBusCount

    seatsLeftCount += leaving
    onBusCount -= leaving


def isValidPosInt(stringValue):
    '''Returns true if the string input can be turned into an int AND is
    strictly greater than zero.
    Argument:
        stringValue - the user input.
    Returns:
        boolean - true or false
    '''
    if isValidPosIntOrZero(stringValue):
        return int(stringValue) > 0
    return False


def isValidPosIntOrZero(stringValue):
    '''Returns true if the string input can be turned into an int AND is
    greater than or equal to zero.
    Argument:
        stringValue - the user input.
    Returns:
        boolean - true or false
    '''
    if not isinstance(stringValue, (str, int)):
        return False

    try:
        maybeInt = int(stringValue)
    except (TypeError, ValueError):
        return False
    else: # else if it got converted to int, check if positive
        return maybeInt >= 0


def isValidNumStops(stringValue):
    '''Returns true if number of stops is >= 2.
    Argument:
        stringValue - the user input.
    Returns:
        boolean - true or false
    '''
    return isValidPosInt(stringValue) and int(stringValue) >= 2


def isValidRouteNumber(stringValue):
    '''A route number is valid if it is > 0.
    Argument:
        stringValue - the user input.
    Returns:
        boolean - true if valid pos int, false otherwise
    '''
    return isValidPosInt(stringValue)


def isValidNumLeaving(stringLeaving, isLastStop = False):
    '''If last stop, all passengers must get off. If not the last stop, chcek that number leaving
     is not greater than that on the bus.
    Arguments:
        leaving - int, number of passengers leaving the bus
        isLastStop - boolean, tells whether it is the last stop or not
    Returns:
        boolean - true or false.
    '''
    if not isValidPosIntOrZero(stringLeaving):
        print("Invalid number of passengers. Please enter a positive integer.")
        return False

    leaving = int(stringLeaving)
    if isLastStop and not leaving == onBusCount:
        print("This is the last stop. There should be", onBusCount, "passengers leaving.")
        return False # leaving == busCount

    if leaving > onBusCount: # leaving <= onBusCount
        print("Invalid number of passengers. Only", onBusCount, "passengers were on the bus.")
        return False

    # else, if it got past these two tests, return true
    return True


def ratioHappyToUnhappy():
    '''Returns ratio of happy to unhappy customers.
    Returns:
        string to two decimal places
    '''
    if unhappyCustomers == 0:
        return "0.00"
    return "{0:.2f}".format(happyCustomers / unhappyCustomers)



# -----------------------------------------------------------------------------------------------------------
# HERE are the loops of the main program, encapsulated for easier reading in the client code (main function).


def inputRouteNumber():
    ''' Loops until we get a valid route number.
    Returns:
        valid route number (> 0)
    '''
    routeNumber = input("Please enter the route number: ")
    while not isValidRouteNumber(routeNumber):
        print("Invalid route number. Please enter a positive integer.")
        routeNumber = input("Please enter the route number: ")
    return int(routeNumber)


def inputLastStop():
    '''Input until we get a valid last stop number.
     Returns:
         amount of stops on the route (>= 2)
    '''
    lastStop = input("\nPlease enter the number of stops on this route: ")
    while not isValidNumStops(lastStop):
        print("Invalid number of stops. There must be at least two stops on the route.")
        lastStop = input("Please enter the number of stops on this route: ")
    return int(lastStop)


def beginBusRoute(lastStop):
    '''Loops until we reach the last stop, asking the number of passengers who are waiting/leaving
    at a particular stop. Makes sure valid input is obtained.
    '''
    for currentStop in range(1, lastStop+1): # until we reach last stop

        if not currentStop == 1:
            print("\nHow many passengers left the bus at stop #", currentStop, "? ", end="", sep="")
            leavingPassengers = input()
            while not isValidNumLeaving(leavingPassengers, isLastStop = currentStop == lastStop):
                print("How many passengers left the bus at stop #", currentStop, "? ", end="", sep="")
                leavingPassengers = input()
            leavingPassengers = int(leavingPassengers)

            getOffBus(leavingPassengers)

        if not currentStop == lastStop:
            if currentStop == 1:
                print("\n")
            print("How many passengers were waiting for the bus at stop #", currentStop, "? ", end="", sep="")
            waitingPassengers = input()
            while not isValidPosIntOrZero(waitingPassengers):
                print("Invalid number of passengers. Please enter a positive integer.")
                print("How many passengers were waiting for the bus at stop #", currentStop, "? ", end="", sep="")
                waitingPassengers = input()
            waitingPassengers = int(waitingPassengers)

            # updating seatsLeftCount, happy/unhappy passengers, and onBusCount
            getOnBus(waitingPassengers)




def displayBusData(routeNumber):
    # printing the "ending" output
    print("\n\n-----------------------------------------------------------------------")
    print("Route number: ", routeNumber, sep="")
    print("Happy customers: ", happyCustomers, sep="")
    print("Unhappy customers: ", unhappyCustomers, sep="")
    print("Ratio of happy to unhappy customers: ", ratioHappyToUnhappy(), "\n", sep="")



def main():
    routeNumber = inputRouteNumber()
    lastStop = inputLastStop()
    beginBusRoute(lastStop)
    displayBusData(routeNumber)



if __name__ == "__main__":
    main()