

def getValidX():
    x = -1

    while x < 0 or x > 1:
        num = input("Enter a number between 0 and 1: ")
        try:
            x = float(num)
        except ValueError:
            print("Invalid. ", end="")
    return x



def chaos(x):
    values = []
    for i in range(10):
        x = 3.9 * x * (1 - x)
        values.append(x)
    return values



def printTable():
    xsChaosPairs = {}

    numXs = 2
    #for i in range(numXs):
    #    x = getValidX()


    print("{0<:13}         {1<:13}         {2<:13}  ".format("index", 0.25, 0.26))
    print("index    0.25         0.26")
    print("----------------------------")

    #for n in range(len(xValues)):
    #    print("  {0}    {1:<8}     {2:<8}".format(n+1, ))



if __name__ == "__main__":

    values = chaos(0.25)
    printTable()