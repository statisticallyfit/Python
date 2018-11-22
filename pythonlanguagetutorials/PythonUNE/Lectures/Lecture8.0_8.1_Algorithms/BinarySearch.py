


def binSearch(values, iFrom, iTo, target):
    if iFrom > iTo:
        return -1

    iMid = (iFrom + iTo) // 2
    if values[iMid] == target:
        return iMid
    elif values[iMid] <= target:
        return binSearch(values, iMid + 1, iTo, target) # search in upper half
    else:
        return binSearch(values, iFrom, iMid - 1, target)


def binarySearch(values, target):
    return binSearch(values, 0, len(values)-1, target)


if __name__ == "__main__":
    vals = [-5, -3, -1, 0, 1, 1, 3, 3, 4, 4, 4, 7, 7, 9, 9, 35] # [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    print(binarySearch(vals, 9))
    print(binarySearch(vals, 23))

