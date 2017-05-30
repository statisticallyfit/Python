# Program to determine the routes that would most benefit from an additional bus
# Author: David Paul
# Date: 2016-12-05

import sys

def readRouteData(filename):
    """
      Reads route number and happy ratio from each line of the given file,
      raising an error if a line has the incorrect format or a route is listed
      more than once.

      Arguments:
      filename -- The name of the file to read the route information from

      Returns a list of dictionaries, with each dictionary containing the following keys:
        - route_number: The route number read from the file
        - happy_ratio:  The happy ratio associated with that route

      Raises:
        ValueError -- if data is in the incorrect format
        IOError -- if there is a problem reading the file
    """
    routeData = []
    readRoutes = []
    fileData = open(filename) # @me potential IOError raised here
    for line in fileData:
        split = line.split(",")
        route = int(split[0]) # @me potential ValueError raised here
        if route in readRoutes:
            raise ValueError("File cannot contain duplicate routes") # @me manual ValueError raised here.
        readRoutes += [route]
        ratio = float(split[1]) # @me potential ValueError raised here.
        routeDict = {}
        routeDict["route_number"] = route
        routeDict["happy_ratio"] = ratio
        routeData += [routeDict]
    fileData.close()
    return routeData

def ratioComesBefore(ratio1, ratio2):
    """
      Determines if the first ratio given as a parameter should be sorted before the second one.

      A ratio that is <=0 comes after any positive ratio, otherwise the smallest positive ratio comes first.

      Arguments:
      ratio1 -- the ratio to check for
      ratio2 -- the ratio to check against

      Returns True if ratio1 should be sorted before ratio2, False otherwise
    """
    if ratio2 <= 0:
        return True
    if ratio1 <= 0:
        return False
    return ratio1 < ratio2

def sortRouteData(route_data):
    """
      Sorts the given route_data by happy_ratio (in place).

      A ratio that is <=0 comes after any positive ratio, otherwise the smallest positive ratio comes first.

      Arguments:
      route_data -- A list of dictionaries to sort, where each dictionary has the following keys:
        - route_number: The route number read from the file
        - happy_ratio:  The happy ratio associated with that route

      Returns the sorted route_data list
    """
    for i in range(1, len(route_data)):
        j = i
        while j > 0 and ratioComesBefore(route_data[j]["happy_ratio"], route_data[j - 1]["happy_ratio"]):
            route_data[j - 1], route_data[j] = route_data[j], route_data[j - 1]
            j = j - 1
    return route_data

def readNonNegativeInteger(prompt, error_prompt):
    """
      Reads a positive integer value from the user, giving another opportunity if the user enters an incorrect value.

      Arguments:
      prompt -- The prompt to display when asking the user to enter a value
      error_prompt -- The prompt to display if the user enters an invalid value before asking them again

      Returns the positive integer value entered by the user
    """
    n = -1
    try:
        n = int(input(prompt))
    except ValueError:
        n = -1
    if n < 0:
        # User entered an invalid value for n. Display error and ask them again
        print(error_prompt)
        n = readNonNegativeInteger(prompt, error_prompt)
    return n





if __name__ == "__main__":
    # Read route information, exiting if there is an error
    try:
        routeData = readRouteData("routes_empty1.txt")
    except:
        print("Error reading data.")
        print("Please ensure each line of routes.txt contains a route number, followed by a comma, followed by a happy ratio")
        print("and that no route is repeated throughout the file")
        sys.exit(1)

    # Read in number of routes that can have an extra bus, ensuring it's a value in the range 0..len(route_data)
    numRoutes = readNonNegativeInteger("How many routes can have an extra bus? ", "Invalid value. Please enter a non-negative integer")
    while numRoutes > len(routeData):
        print("Invalid value. There are only {0} possible routes".format(len(routeData)))
        numRoutes = readNonNegativeInteger("How many routes can have an extra bus? ", "Invalid value. Please enter a non-negative integer")

    # Sort route information based on happy_ratio
    sortRouteData(routeData)

    # Output the top num_routes routes that would benefit from an extra bus
    print("You should add buses for the following routes:")
    for i in range(numRoutes):
        print("\t{0}".format(routeData[i]["route_number"]))
