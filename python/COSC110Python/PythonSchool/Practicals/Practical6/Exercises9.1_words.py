
# 9.1: prints only words with more than 20 chars, not counting whitespace
def printWordsGreaterTwentyChars():
    '''Prints only words with more than 20 chars'''
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

printWordsGreaterTwentyChars()




# 9.2: prints only words with no 'e' and computes percentage
def wordsWithNoE():
    '''Returns percentage of words with no 'e' in the wordlist.
    Prints all words with no 'e'.
    '''
    fin = open("words.txt")
    count = 0
    countNoE = 0

    for line in fin:
        word = line.strip()
        if not 'e' in word:
           countNoE += 1
           print(word)
        count += 1
    return countNoE / count * 100

#print("\n\nAll these words have no 'e': ")
#print("\n\nPercentage: ", wordsWithNoE())




# 9.3 -- avoids

def avoids(word, forbidden):
    '''returns true if word doesn't use any of the forbidden letters'''
    return not any(letter in forbidden for letter in word)

assert avoids("peaches", "diff")
assert not avoids("summer", "silk")




# 9.4 --
def usesOnly(word, available):
    '''returns true if word contains only letters in the list'''
    return all(letter in available for letter in word)

def usesOnly3(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def usesOnly2(word, available):
    return set(word).issubset(set(available))

def printWordsAvailable(available):
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if usesOnly(word, available):
            count += 1
            print(word)
    print(count)


assert usesOnly("summer", "many summers")
assert usesOnly("peanut", "peanut")
assert not usesOnly("peaches and pie", "zealots")
assert usesOnly2("summer", "many summers")
assert not usesOnly2("peaches and pie", "zealots")

print("\n\nAvailable: hoealfalfa: ")
printWordsAvailable("Hoe alfalfa")
print("\n\nAvailable: acefhlo")
printWordsAvailable("acefhlo")




# 9.5 - uses all

def usesAll(word, required):
    ''' returns True if word contains all letters found in required letters.'''
    return all(letter in word for letter in required)

def usesAll2(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def usesAllSets(word, required):
    return set(word).intersection(set(required)) == set(required)

def usesAllSets2(word, required):
    return set(word).issuperset(set(required))

def usesAll3(word, required):
    return usesOnly(required, word)
# word.issuperset(required)  --- usesOnly
# required.issuperset(word)  --- usesAll


def printWordsRequired(required):
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if usesAll(word, required):
            count += 1
            print(word)
    print(count)



assert usesAll("abstemious", "aeiou")
assert not usesAll("abstemious", "aeiouy")
assert usesAll2("aureaiodine", "aeiou")
assert not usesAll2("perfect", "perfect life")
assert usesAllSets("aureaiodine", "aeiou")
assert not usesAllSets("perfect", "perfect life")
assert usesAllSets2("aureaiodine", "aeiou")
assert not usesAllSets2("perfect", "perfect life")
assert usesAll3("aureaiodine", "aeiou")
assert not usesAll3("perfect", "perfect life")


print("\n\nRequired: aeiou")
printWordsRequired("aeiou")
print("\n\nRequired: aeiouy")
printWordsRequired("aeiouy")





# 9.6 - abecedarian

def isAbecedarian(word):
    return word == "".join(sorted(word))

def countAbecedarianWords():
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if isAbecedarian(word):
            print(word)
            count += 1
    return count

assert not isAbecedarian("apricot")
assert isAbecedarian("abcdeeeeffghiiiii")
print("\n\nCount abecedarian: ", countAbecedarianWords())