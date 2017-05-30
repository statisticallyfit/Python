# exercise 8.3
# expects cleaned string
def isPalindrome(word):
    return word[:] == word[::-1]


print(isPalindrome("racecar"))
print(isPalindrome("docnoteidissentafastneverpreventsafatnessidietoncod"))




# exercise 8.5 - caesar cypher
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



print(rotateWord("melon", -10))
print(rotateWord("IBM", -1))
print(rotateWord("zfly", 5))