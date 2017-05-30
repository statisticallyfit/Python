import time


def handleBadSize(values):
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return (values[0], None)
    elif len(values) == 2:
        return (values[0], values[1]) if values[0] < values[1] else (values[1], values[0])


# note: fails for duplicates
# method 1: find, remove find: find index of min, remove it, then find index of
# new min the in list. After we have the second index, put back removed value
# and adjust second index for that reinsertion.
def removeFindTwoMins(values):
    if len(values) in [0, 1, 2]:
        return handleBadSize(values)

    # find index of min and remove that item
    mini = min(values)
    iMin = values.index(mini)
    values.remove(mini)

    # find index of next min
    nextMin = min(values)
    iNextMin = values.index(nextMin)


    values.insert(iMin, mini)

    # put smallest back into list and adjust second index if necessary.
    if iMin <= iNextMin:
        iNextMin += 1

    ##values.insert(iNextMin, nextMin)

    return iMin, iNextMin


# note: fails for duplicates
# method 2: sort, get mins, get indices. Sort list, get two smallest, find indices
# in the original list
def sortFindTwoMins(values):
    if len(values) in [0, 1, 2]:
        return handleBadSize(values)



    # sort a copy of values
    valuesSorted = sorted(values)

    # get two smallest
    mini, nextMini = valuesSorted[0], valuesSorted[1]

    # find their indices in original list
    iMin = values.index(mini)
    iNextMin = values.index(nextMini)

    # return the two indices
    return iMin, iNextMin


# method 3: walk: examine each value in order, keep track of two min values, update
# as you get to smaller value.
def walkFindTwoMins(values):
    if len(values) in [0, 1, 2]:
        return handleBadSize(values)



    #examine each value in order
    # keep track of indices of two smallest so far
    # update when new smaller is found
    # return the two indices

    #firstMin, nextMin, iFirst, iNext = 0,0,0,0

    if values[0] < values[1]:
        firstMin, nextMin = values[0], values[1]
        iFirst, iNext = 0, 1
    else:
        nextMin, firstMin = values[0], values[1]
        iNext, iFirst = 0, 1

    for i in range(2, len(values)):
        if values[i] < firstMin:
            nextMin = firstMin # shifting
            firstMin = values[i]
            iNext = iFirst
            iFirst = i
        elif firstMin < values[i] < nextMin:
            nextMin = values[i] # no need to update the firstmind
            iNext = i
        # else if values[i] is larger than both skip it.

    return iFirst, iNext




if __name__ == "__main__":
    # method 1
    counts1 = [434,124,785,346,34,15,12, 178,233,333,58,3455]
    counts2 = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    dups = [434,124,785,346,34,15,15, 12,12, 15, 178,233,333,58,3455]

    assert removeFindTwoMins(counts1) == (6, 5)
    assert removeFindTwoMins(counts2) == (6, 7)
    assert not removeFindTwoMins(dups) == (7, 5) # see, doesn't work for duplicates.

    # note: see this for difference between is None and == None:
    # http://jaredgrubb.blogspot.ro/2009/04/python-is-none-vs-none.html

    assert removeFindTwoMins([]) is None
    assert removeFindTwoMins([]) == None
    assert removeFindTwoMins([1]) == (1, None)
    assert removeFindTwoMins([3,1]) == (1, 3)
    assert removeFindTwoMins([1,3]) == (1, 3)
    assert removeFindTwoMins([3,3]) == (3, 3)

    # method 2
    assert sortFindTwoMins(counts1) == (6, 5)
    assert sortFindTwoMins(counts2) == (6, 7)
    assert not sortFindTwoMins(dups) == (7, 5)
    assert sortFindTwoMins([]) is None
    assert sortFindTwoMins([1]) == (1, None)
    assert sortFindTwoMins([3,1]) == (1, 3)
    assert sortFindTwoMins([1,3]) == (1, 3)
    assert sortFindTwoMins([3,3]) == (3, 3)

    # method 3 - note - works for duplicates, with other 2 don't!
    assert walkFindTwoMins(counts1) == (6, 5)
    assert walkFindTwoMins(counts2) == (6, 7)
    assert walkFindTwoMins(dups) == (7, 5)
    assert walkFindTwoMins([]) is None
    assert walkFindTwoMins([1]) == (1, None)
    assert walkFindTwoMins([3,1]) == (1, 3)
    assert walkFindTwoMins([1,3]) == (1, 3)
    assert walkFindTwoMins([3,3]) == (3, 3)


    '''
    # read in sea level pressures
    seaLevelPressures = []
    fIn = open("seaLevelPressures.txt")
    for line in fIn:
        cleaned = line.strip()
        if cleaned: # if not empty string, then add it as float
            seaLevelPressures.append(float(cleaned))
    fIn.close()

    for func in [removeFindTwoMins, sortFindTwoMins, walkFindTwoMins]:
        start = time.perf_counter()
        func(counts2)
        end = time.perf_counter()
        print("Diff time for: ", str(func), " =   ", (end - start)*1000) # convert to milliseconds
        '''