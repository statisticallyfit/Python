
# Format method
print("Hello {0}".format("anything 23"))
#print("The story of {0}, {1}, and {c}".format(a, b, c=d))

# note: deeper understanding here: https://pyformat.info/
# note another tutorial: http://www.python-course.eu/python3_formatted_output.php

# Format specifier:
# [[fill] align]   [sign]   [#]  [0]  [width]  [.precision] [type]

### note: 0 is the shortcut for ones before.
# fill:
# align: < (left), > right, ^ center, = after sign
# sign: + (all nums), -(neg), '' (leading space)
# # alternate form for formatting
# 0: same as alignment type '=' and fill of '0'
# width: min width of field
# precision: how many digits after decimal.
# type: how data should be presented: defaults to string

print("Hello {0}! {1}/2 is {2:.2f}".format("Fred", 5.5, 5.5/2))
# width: 10 chars long
print("Hello {0}! {1}/2 is {2:10.2f}".format("Fred", 5.5, 5.5/2))
# fill: zero padding, 10 chars long
print("Hello {0}! {1}/2 is {2:010.2f}".format("Fred", 5.5, 5.5/2))






# Conditionals flattened:
import math


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def squareRoot(n):
    return math.sqrt(n) if n > 0 else 0

print(squareRoot(100), squareRoot(-16), squareRoot(3))



initialValues = list(range(10))

def squares(lst):
    squares = []
    for value in lst:
        squares.append(value * value)
    return squares

def squaresGood(lst):
    return [x * x for x in lst]

def pairs(): # NOTE: y is nested under the x-loop.
    return [(x,y) for x in range(3) for y in [2,4,1] if x != y]

def pairs2(): # NOTE: x is nested under the y-loop.
    return [(x,y) for y in [2,4,1] for x in range(3) if x != y]

print(squares(initialValues))
print(squaresGood(initialValues))
print(pairs())
print(pairs2())



# note: now loops go from right to left because left is higher (inside)
matrix = [[0,1,2], [3,4,5], [6,7,8]]
print([[row[i] for row in matrix] for i in range(len(matrix))])





# Generators:
# # use parantheses, they are similar to list comprehensions
# value generated only when it is needed (unlike list comp)
genSquares = (x ** 2 for x in range(10))
#print(list(genSquares))
for square in genSquares:
    print(square)
print(list(genSquares)) # none left (like iterator), only store one in memory at a time.





# LAMBDA:
def makeIncrementer(n):
    return lambda x: x + n # takes parameter x adds it to n

print("\n", makeIncrementer(10)(4))
f = makeIncrementer(1)
g = makeIncrementer(5)
print(f(7), g(7))






# Pass by obj reference Example 1:
def modifyList(listToModify):
    listToModify.append(7)
    print("inside: ", listToModify)
    listToModify = [1,2,3]
    print("inside: ", listToModify)

### listTOModify points to area in memory which points to reference to x
### append 7 to x's list
### assigning [1,2,3] to listToModify sets up list in memory [1,2,3]
# and listToModify is assigned to point to that list.
x = [4,5,6]
modifyList(x)
print(x)
# pass by obj reference: can modify the caller list, but cannot REASSIGN





# Pass by obj reference Example 2:
def f(n):
    n = 3
a = 1
f(a)
print(a) # still 1

listA = [0]
listB = listA # they are pointing to same area in memory now (lists characteristic)
listB.append(a) # note: modifications change both lists as they point to same areas in memory.
# note: in reference passing, they ARE the same areas in memory so reassignments are also permanent.
print(a)
print(listA)
print(listB)

listB = [0,1,2] # note: reassigning it makes it point to somewhere else, so listA does not get modified.
print(listA)
print(listB)






# RECURSION:
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# iteration is faster than recursion because no need to store activation records.
def fibonacciIterative(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fibonacci(4), fibonacciIterative(4))
print(fibonacci(8), fibonacciIterative(8))
print(fibonacci(2), fibonacciIterative(2))





# recursion example: quicksort:
# basic idea: split list into two parts: left has all less than pivot, right has all greater than pivot.
# then recursively sort both halves.

def pivot(theList, a, b):
    pivotValue = theList[(a + b) // 2]
    i, j = a - 1, b + 1

    while True:
        i, j = i+1, j-1

        # iterate until you find item greater than pivot in left half
        # and item less than pivot in right half then swap them.
        while theList[i] < pivotValue:
            i += 1
        while theList[j] > pivotValue:
            j -= 1

        if i >= j:
            return j
        theList[i], theList[j] = theList[j], theList[i] # swapping them

# note:
# choose pivot from middle
# make sure everything to left is less than pivot, and everything higher is greater than it (swapping)
# apply quicksort again to left and right halves.
def quickSortHelper(theList, a, b):
    if a < b:
        pivotIndex = pivot(theList, a, b)
        quickSortHelper(theList, a, pivotIndex) # the left half
        quickSortHelper(theList, pivotIndex + 1, b) # the right half
    return 1

def quickSort(listToSort):
    return quickSortHelper(listToSort, 0, len(listToSort) - 1) # providing begin/end indexes


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

# helper links:
# http://www.algolist.net/Algorithms/Sorting/Quicksort
# see my sheet on desk