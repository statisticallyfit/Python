

def minOrMax(values, findMin=True):

    iMinOrMax = 0

    if findMin:
        for i in range(1, len(values)):
            if values[i] < values[iMinOrMax]:
                iMinOrMax = i
    else:# find max
        for i in range(1, len(values)):
            if values[i] > values[iMinOrMax]:
                iMinOrMax = i
    return iMinOrMax, values[iMinOrMax]



if __name__ == "__main__":

    vals = [4, 3, 2, 4, 3, 8, 1, 5]
    assert minOrMax(vals, findMin=True) == (6, 1)
    assert minOrMax(vals, findMin=False) == (5, 8)