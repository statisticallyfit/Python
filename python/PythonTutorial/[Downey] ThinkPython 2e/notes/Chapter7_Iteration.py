

def collatzConjecture(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    print(n, " --- END")


collatzConjecture(3)
collatzConjecture(4)
collatzConjecture(16)



# --------------------------------------------------------------------------------------------

# newton root approximation method
def newtonRootApprox(number, guess):
    epsilon = 0.0000000000000000000000000000000000000000000000000001

    a = float(number)
    x = float(guess)

    while True:
            print(x)
            y = (x + a/x)/2
            if(abs(x - y) < epsilon):
                    break
            # otherwise set x = y
            x = y # to get new updated estimate
    print(x)

print("\n\nNewton: ")
newtonRootApprox(35, 70)