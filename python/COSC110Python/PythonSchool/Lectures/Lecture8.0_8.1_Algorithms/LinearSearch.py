

def linearSearch(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1 # not in the list



if __name__ == "__main__":
    vals = [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    print(linearSearch(vals, 9))
    print(linearSearch(vals, 23))

    vals = [-5, -3, -1, 0, 1, 1, 3, 3, 4, 4, 4, 7, 7, 9, 9, 35]
    print(linearSearch(vals, 9))
    print(linearSearch(vals, 23))


