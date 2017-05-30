
# recursion example: quicksort:
# (1) basic idea: split list into two parts: left has all less than pivot,
# right has all greater than pivot.
# then recursively sort both halves.

def pivot(values, iLow, iHigh):
    pivotValue = values[(iLow + iHigh) // 2]
    i, j = iLow - 1, iHigh + 1

    while True:
        i, j = i+1, j-1

        # (2) iterate until you find item greater than pivot in left half
        # and item less than pivot in right half then swap them.
        while values[i] < pivotValue:
            i += 1
        while values[j] > pivotValue:
            j -= 1

        if i >= j:
            return j
        values[i], values[j] = values[j], values[i] # swapping them
        print("swapped {0} and {1}: {2}".format(values[i], values[j], values))



# note:
# choose pivot from middle
# make sure everything to left is less than pivot, and everything higher is greater than it (swapping)
# apply quicksort again to left and right halves.
def quickSortHelper(values, iLow, iHigh):
    print("sorting range: [{0}, {1}],   {2}".format(iLow, iHigh, values))

    if iLow < iHigh:
        iPivot = pivot(values, iLow, iHigh)
        print("pivot index: ", iPivot)
        quickSortHelper(values, iLow, iPivot) # the left half
        quickSortHelper(values, iPivot + 1, iHigh) # the right half
    return 1

def quickSort(values):
    return quickSortHelper(values, 0, len(values) - 1) # providing begin/end indexes


listToSort = [13, 3, 7, 8, 19, 78, 3, 46, -9, 0, 32]
print("\n")
print(listToSort)
quickSort(listToSort)
print(listToSort)

listToSort = [1, 12, 5, 26, 7, 14, 3, 7, 2]
print("\n")
print(listToSort)
quickSort(listToSort)
print(listToSort)