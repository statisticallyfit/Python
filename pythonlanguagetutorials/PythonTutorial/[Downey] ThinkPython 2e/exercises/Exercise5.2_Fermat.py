


# part 1
def checkFermat(a, b, c, n):
    if(n > 2 and (a**n + b**n == c**n)):
        print("n > 2: Fermat was wrong!")
    elif (n > 2 and (a**n + b**n != c**n)):
        print("n > 2: Fermat was right, it didn't work.")
    else:
        print("n <= 2: no test.")



def main():
    # part 1
    checkFermat(3, 4, 5, 2)
    checkFermat(3, 4, 5, 6)
    checkFermat(9, 8, 17, 1)
    checkFermat(8, 9, 454, 44)

    # part 2
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    n = int(input("n = "))
    print("\nInput results: ", sep="")
    checkFermat(a, b, c, n)



if __name__ == "__main__":
    main()