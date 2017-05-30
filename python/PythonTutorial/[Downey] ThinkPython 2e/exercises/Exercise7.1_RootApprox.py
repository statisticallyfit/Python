import math
import string



# newton root approximation method
def sqrtApprox(a, x):
    epsilon = 0.0000000000000000000000000000000000000000000000000001

    while True:
            y = (x + a/x)/2
            if(abs(x - y) < epsilon):
                    break
            x = y # otherwise set x = y to get new updated estimate
    return x



##### HELP Can't get this  thing right!!!!!

def squareRootTable():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(8):
        # printing (a)
        a = float(a + 1)
        print(a, end=" ")

        # printing approximation
        approx = sqrtApprox(a, a)
        strApprox = str(round(approx, 11))
        print("{0:<13}".format(strApprox), end=" ")
        #print(strApprox.ljust(13 - len(strApprox), ' '), end=" ")

        # printing actual value
        actual = math.sqrt(a)
        strActual = str(round(actual, 11))
        diff = abs(approx - actual)
        print("{0:<13}".format(strActual), end=" ")
        #print(strActual.ljust(13 - len(strActual), ' '), end=" ")

        # printing diff
        print(diff)

print("\n\nNewton: ")
squareRootTable()