

# note: shifts the index each time. While the adjacent value in front is less than
# note - previous value, then continue swapping until the "adjacent" one gets to its
# note - correct position - forms a complete sort. The adjacent item bubbles its way down the list
# note - to its final correct position.
def insertionSort(values):
    for i in range(1, len(values)): # n - 1 passes
        j = i
        while j > 0 and values[j] < values[j - 1]:
            values[j - 1], values[j] = values[j], values[j - 1]
            print("swapped {0} and {1}: {2}".format(values[j], values[j-1], values))
            j -= 1



if __name__ == "__main__":
    vals = [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    insertionSort(vals)
    print(vals)