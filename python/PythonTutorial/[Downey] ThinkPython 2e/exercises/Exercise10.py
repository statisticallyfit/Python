
import random
import time


# 1 -----------------------------------------------------------------------

# take nested list and sum elements total
def nestedSum(listOfLists):
    total = 0

    for aList in listOfLists:
        for elem in aList:
            total += elem
    return total

# NOT more protected if no nesting
def solutionNestedSum(listOfLists):
    total = 0
    for nested in listOfLists:
        total += sum(nested)
    return total

print(nestedSum([[1,2], [3], [4,5,6]]))
#print(solutionNestedSum([[1, 2], 3, [4, 5, 6]]))



# 2 -----------------------------------------------------------------------

def cumSum(lst):
    cumLst = lst[:]

    for i in range(len(lst)):
        if i != 0:
            cumLst[i] += cumLst[i-1]

    return cumLst


print(cumSum([1,2,3,4,5]))

# 3 -----------------------------------------------------------------------

# safe operation
def middle(lst):
    return lst[1:-1]

print(middle([1,2,3,4,5]))
print(middle([1]))
print(middle([]))

# 4 -----------------------------------------------------------------------

def chop(lst):
    del lst[0]; del lst[-1]

t1 = [1,2,3,4]
print(chop(t1))
print(t1)
t2 = [3,4,-9,2]
chop(t2)
print(t2)
# note: makes error
# t3 = []
# chop(t3)
# print(t3)

# 5 -----------------------------------------------------------------------

def isSorted(lst):
    return lst == sorted(lst)

# 6 -----------------------------------------------------------------------

def isAnagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(isAnagram("melon", "lemon"))
print(isAnagram("pipe", "gateing"))


# 7 -----------------------------------------------------------------------

# range is save for negatives or zero
def hasDuplicates(lst):

    adjacents = sorted(lst)
    for i in range(len(adjacents) - 1):
        if adjacents[i] == adjacents[i+1]:
            return True
    return False

print(hasDuplicates([1,3,6,4,3,8,4]))
print(hasDuplicates([2,3,5,8,90, -1]))
print(hasDuplicates([]))
print(hasDuplicates([1]))
print(hasDuplicates([1,1]))

# 8 -----------------------------------------------------------------------

# generate a limit of n random birthdays
def randomBirthdays(limit):
    bDays = []
    for counter in range(limit):
        # randint(a, b) generates N in the interval: a <= N <= b
        bDays.append(random.randint(1, 365))
    return bDays

# counts which samples have duplicate birthdays
def countSamplesWithDuplicates(numStudents, numSimulations):
    count = 0
    for sim in range(numSimulations):
        randBdaysList = randomBirthdays(numStudents)
        if hasDuplicates(randBdaysList):
            count += 1
    return count


print(countSamplesWithDuplicates(23, 10)/10)
print(countSamplesWithDuplicates(23, 20)/20)
print(countSamplesWithDuplicates(23, 20)/20)
print(countSamplesWithDuplicates(23, 40)/40)
print(countSamplesWithDuplicates(23, 90)/90)
print(countSamplesWithDuplicates(23, 1000)) # always near 0.5

# 9 -----------------------------------------------------------------------


def appendFromFile():
    path = '/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/'
    file = open(path + 'words.txt')
    words = []

    for line in file:
        wordList = line.strip().split(" ")
        for word in wordList:
            words.append(word)
    return words

def addFromFile():
    path = '/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/'
    file = open(path + 'words.txt')
    words = []

    for line in file:
        wordList = line.strip().split(" ")
        words += wordList
    return words

def getElapsedTime(f):
    startTime = time.time()
    f()
    return time.time() - startTime

print(getElapsedTime(appendFromFile))
print(getElapsedTime(addFromFile))



# 10 -----------------------------------------------------------------------

## HELP how to make bisect so it returns the index in the actual place in original list?
'''
def inBisect(sortedList, target):
    indexes = range(len(sortedList))

'''

def bisector(sortedList, target):
    if len(sortedList) == 0:
        return -1

    mid = len(sortedList) // 2

    if sortedList[mid] == target:
        return mid

    if sortedList[mid] < target:
        # mid is less than target so search upper
        return bisector(sortedList[mid + 1:], target)
    else:
        # mid is greater than target so search lower
        return bisector(sortedList[0:mid], target)


print("\ninBisect: ", bisector([1, 2, 4, 5, 6, 7, 8, 8, 8, 9, 40, 58, 90], 7))

wordList = addFromFile()
print(bisector(sorted(wordList), "Grethel"))


# 11 -----------------------------------------------------------------------

def isReversePair(elems1, elems2):
    return elems1[:] == elems2[::-1]


# 12 -----------------------------------------------------------------------
# does the interlock appear in the word list?
def isInterlockInWordList(wordList, word):
    evens = word[::2]
    odds = word[1::2]
    sortedWords = sorted(wordList)
    return isInBisect(sortedWords, evens) and isInBisect(sortedWords, odds)


def isInterlockInWordListGeneral(wordList, word, n=3):
    # n = number of interleaved words, step size
    for i in range(n):
        inter = word[i::n]
        if not isInBisect(sorted(wordList), inter):
            return False
    return True


def isInBisect(sortedList, target):
    if len(sortedList) == 0:
        return False

    mid = len(sortedList) // 2

    if sortedList[mid] == target:
        return True

    if sortedList[mid] < target:
        # mid is less than target so search upper
        return bisector(sortedList[mid + 1:], target)
    else:
        # mid is greater than target so search lower
        return bisector(sortedList[0:mid], target)

print("\n\nINTERLOCK: ")
wordList = addFromFile()
for word in wordList:
    if isInterlockInWordList(wordList, word):
        print(word, word[::2], word[1::2])

print("\n\nGENERAL INTERLOCK: ")
for word in wordList:
    if isInterlockInWordListGeneral(wordList, word, n=3):
        print(word, word[0::3], word[1::3], word[2::3])

