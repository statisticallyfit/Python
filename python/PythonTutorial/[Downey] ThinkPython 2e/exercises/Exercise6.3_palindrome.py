import string



def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# ----------------------------
def cleanWord(word):
    return(removeSpaces(removePunctuation(word.lower())))

def removeSpaces(word):
    wordNoSpace = ""
    for pos in range(len(word)):
        if not word[pos] == ' ':
            wordNoSpace += word[pos]
    return wordNoSpace

def removePunctuation(word):
    wordNoPunct = ""
    for pos in range(len(word)):
        if word[pos] not in string.punctuation:
            wordNoPunct += word[pos]
    return wordNoPunct


# ----------------------------

def isPalindrome(word):
    return isPalin(cleanWord(word))


def isPalin(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return isPalin(middle(word))



'''
clean = cleanWord("Doc, note. I dissent. A fast never prevents a fatness. I diet on Cod.")
print(isPalin(clean))
print(isPalindrome(clean))
'''
assert isPalindrome("Doc, note. I dissent. A fast never prevents a fatness. I diet on Cod."), "check test 1"
assert isPalindrome("racecar"), "check test 2"
assert not isPalindrome("backwards"), "check test 3"
assert isPalindrome("redivider"), "check test 4"
assert isPalindrome("noon"), "check test 5"
