

def mSort(values, leftValues, rightValues):
    i, j, k = 0, 0, 0

    while i < len(leftValues) and j < len(rightValues):
        if leftValues[i] < rightValues[j]:
            values[k] = leftValues[i]
            i += 1
        else:
            values[k] = rightValues[j]
            j += 1
        k += 1

    while i < len(leftValues):
        values[k] = leftValues[i]
        i += 1
        k += 1
    while j < len(rightValues):
        values[k] = rightValues[j]
        j += 1
        k += 1


# note: just keeps calling itself to get the list split up then calls merging algo
# note - to merge the intermediary pieces together.
def mergeSort(values):
    if len(values) > 1:
        iMid = len(values) // 2
        left = values[0:iMid]
        right = values[iMid: ]
        mergeSort(left)
        mergeSort(right)
        mSort(values, left, right)





if __name__ == "__main__":
    vals = [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    mergeSort(vals)
    print("values sorted: ", vals)
