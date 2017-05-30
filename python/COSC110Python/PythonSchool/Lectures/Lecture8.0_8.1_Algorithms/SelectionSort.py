
'''
# note: zelle
# note: goes through entire list (unlike insertion sort) to find min index. Then swaps. Then re-starts again from where it left off.
def selectionSort(numbers):
    # sort numbers into ascending order

    n = len(numbers)

    #For each position in the list (except very last)
    for bottom in range(n - 1):
        # find smallest item in nums[bottom] ... nums[n-1]

        iMin = bottom # initialize
        for i in range(bottom + 1, n): # look at each position
            if numbers[i] < numbers[iMin]: # found smaller one
                iMin = i

        # swap smallest item to the bottom
        numbers[bottom], numbers[iMin] = numbers[iMin], numbers[bottom]


'''

# note: lecture
def indexSmallest(values, iLower, iUpper):
    iMin = iLower
    for i in range(iLower + 1, iUpper):
        if values[i] < values[iMin]:
            iMin = i
    return iMin

def selectionSort(values):
    for i in range(len(values)):
        j = indexSmallest(values, i, len(values))
        # swap
        values[i], values[j] = values[j], values[i] # swap at the end
        print("swapped {0} and {1}: {2}".format(values[j], values[i], values))
    return values

if __name__ == "__main__":
    vals = [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    selectionSort(vals)
    print(vals)