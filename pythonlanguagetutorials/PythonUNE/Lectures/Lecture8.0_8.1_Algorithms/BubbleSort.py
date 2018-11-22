
# note: basic idea: starts from end and compares each time with non-changing value on the
# note - left if smaller it swaps them then keeps going till it reaches front of list.
# note - then it moves the left cursor over right one and repeats.
def bubbleSort(values):
    for i in range(len(values)):
        for j in range(len(values) - 1, i,  -1):
            if values[j] < values[i]:
                values[j], values[i] = values[i], values[j]
                # note documentation
                print("swapped {0} and {1}: {2}".format(values[j], values[i], values))


if __name__ == "__main__":
    vals = [1,35,7,9,-3,4,-5,0,1,3,7,9,4,3,-1,4]
    bubbleSort(vals)
    print(vals)