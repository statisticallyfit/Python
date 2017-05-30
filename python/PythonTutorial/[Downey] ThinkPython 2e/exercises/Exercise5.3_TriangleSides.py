


# part 1
def isTriangle(a, b, c):
    if(a > b + c or b > a + c or c > a + b):
        return False
    else:
        return True

def main():
    # part 1
    print(isTriangle(1, 2, 3))
    print(isTriangle(4, 50, 12))

    # part 2
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    print(isTriangle(a, b, c))




if __name__ == "__main__":
    main()