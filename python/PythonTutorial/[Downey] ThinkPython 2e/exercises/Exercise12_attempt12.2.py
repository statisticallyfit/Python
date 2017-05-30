

def readFile(fileName):
    path = '/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/'
    file = open(path + fileName)
    words = []

    for line in file:
        wordList = line.strip().split(" ")
        words += wordList
    return words


# 1 -------------------------------------------------------------------

def frequency(lst):
    d = {}
    for elem in lst:
        d[elem] = d.get(elem, 0) + 1
    return d

def invertDict(d):
    inverse = dict()
    for key in d:
        val = d.get(key)
        inverse.setdefault(val, []).append(key)
    return inverse


def mostFrequent(str):
    t = []
    freqs = frequency(list(str))
    for letter, freq in freqs.items():
        t.append((freq, letter))
    t.sort(reverse=True)

    # getting the actual letters (like map snd in haskell)
    justLetters = []
    for freq, letter in t:
        justLetters.append(letter)
    return justLetters

print(mostFrequent("saaaaaaaaaaaaaaaaaaaaaalkajlkjawerelerlkjerkljeeeeeeeaaaaeiuoiuoiuoiu"))

emma = readFile("emma.txt")
#print(mostFrequent(emma))



# 2 -------------------------------------------------------------------

# anagrams

# part 1
def getAnagrams(wordList, word):
    anagrams = []
    for potential in wordList:
        if sorted(potential) == sorted(word):
            anagrams.append(potential)

    #removeAll(wordList, anagrams) # modifies wordList, to avoid repetition
    return anagrams


def getAllAnagrams(wordList):
    allAnagrams = []

    for word in wordList:
        allAnagrams.append(getAnagrams(wordList, word))

    # removing duplicates
    uniqueAnagrams = []
    for anagramList in allAnagrams:
        if anagramList not in uniqueAnagrams:
            uniqueAnagrams.append(anagramList)

    return uniqueAnagrams

# removes toRemove list and modifies wordList
def removeAll(wordList, toRemove):
    for rem in toRemove:
        wordList.remove(rem)


wordList = readFile("anagrams.txt")
anagrams = getAllAnagrams(wordList)
for lst in anagrams:
    print(lst)




# 1 -------------------------------------------------------------------
# 1 -------------------------------------------------------------------
# 1 -------------------------------------------------------------------
# 1 -------------------------------------------------------------------