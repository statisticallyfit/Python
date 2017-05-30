

def recurse(n, s):
    if n == 0:
        print("(", n, ", ", s, ")", sep="")
        print("S = ", s, sep="")
    else:
        print("(", n, ", ", s, ")", sep="")
        recurse(n-1, n+s)


def main():
    recurse(3, 0)
    print("\n")
    #recurse(-1, 0) # never use negatives because stackoverflow


if __name__ == "__main__":
    main()