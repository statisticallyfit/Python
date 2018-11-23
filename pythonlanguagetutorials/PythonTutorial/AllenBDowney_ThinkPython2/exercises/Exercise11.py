

# 1------------------------------------------------------------------------------------------

def getWordsFromFile(fileName):
    path = '/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/'
    file = open(path + fileName)
    words = []

    for line in file:
        wordList = line.strip().split(" ")
        words += wordList
    return words

def frequency(lst):
    d = {}
    for elem in lst:
        d[elem] = d.get(elem, 0) + 1
    return d

wordList = getWordsFromFile("words.txt")
freq = frequency(wordList)
print(freq)
print("family" in freq)
print("answered" in freq)


# 2------------------------------------------------------------------------------------------

# using setdefault
def invertDict(d):
    inverse = dict()
    for key in d:
        val = d.get(key)
        inverse.setdefault(val, []).append(key)
    return inverse

print(invertDict(freq))

# 3 ------------------------------------------------------------------------------------------

# memoize ackermann
cache = {}
def ackermann(m, n):
    if m == 0:
        return n+1

    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m - 1, ackermann(m, n - 1))
        return cache[m, n]

print(ackermann(1, 10))
print(cache)


# 4 ------------------------------------------------------------------------------------------
def hasDuplicates(lst):
    freq = frequency(lst)
    print(freq)
    for val in freq.values():
        if val > 1:
            return True
    return False

print(hasDuplicates([1,2,3,4,3,3,3,3,4,4,4,4,6,8,8,4,3,6,7,4,6,8,9,5,3,6,8,4,5]))
print(hasDuplicates([1,3,4,6,89]))

def hasDuplicateFaster(lst):
    return len(set(lst)) < len(lst)

print(hasDuplicateFaster([1,2,3,4,3,3,3,3,4,4,4,4,6,8,8,4,3,6,7,4,6,8,9,5,3,6,8,4,5]))
print(hasDuplicateFaster([1,3,4,6,89]))


# 5 ------------------------------------------------------------------------------------------

def rotateWordsInWordList(word, wordDict):
    for i in range(1, 14):
        rotated = rotateWord(word, i)
        if rotated in wordDict:
            print(word, i, rotated)


def rotateWord(word, by):

    # so that we get int between 0 and 25 inclusive
    # so that we can mod 26 wraparound
    def lowToInt(letter): return ord(letter) - ord('a')
    def uppToInt(letter): return ord(letter) - ord('A')
    def intToLow(n): return chr(n + ord('a'))
    def intToUpp(n): return chr(n + ord('A'))

    cipherWord = ""

    for letter in word:
        if letter.isupper():
            cipherWord += intToUpp((uppToInt(letter) + by) % 26)
        elif letter.islower():
            cipherWord += intToLow((lowToInt(letter) + by) % 26)
        else:
            cipherWord += letter # not a letter

    return cipherWord

# HELP why dpesn't this print out?
rotateWordsInWordList("HARD", freq)
print(list(map( (lambda x: rotateWord(x, 3)), freq)))

# 6 ------------------------------------------------------------------------------------------
# 7 ------------------------------------------------------------------------------------------