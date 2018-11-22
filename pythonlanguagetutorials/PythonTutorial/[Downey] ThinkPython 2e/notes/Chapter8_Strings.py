
# 8.6 - searching
def find(word, letter, indexStart=0, indexEnd=-1):
    i = indexStart
    j = len(word) if indexEnd == -1 else indexEnd

    if i > j:
        i, j = j, i # so 11,8 would be 8,11

    while i < j:
        if word[i] == letter:
            return i
        i += 1 # increment
    return -1 # not found



assert find("yellow", "w") == 5
assert find("rumpelstiltskin", "s") == 6
assert find("rumpelstiltskin", "s", 7) == 11
assert find("rumpelstiltskin", "s", 8, 11) == -1
assert find("rumpelstiltskin", "s", 12, 8) == 11




# 8.7 counting looping
def count(word, searchLetter):
    count = 0

    for letter in word:
        if letter == searchLetter:
            count += 1
    return count


print("count: ", count("banana", "n"))
print("count: ", count("rumpelstiltskin", "s"), count("rumpelstiltskin", "t"))





# 8.11 traversal reverse (debug)

def isReversed(word1, word2):
    if len(word1) != len(word2):
        return False

    length = len(word1)
    wasReversed = True

    reversedWord2 = "".join(list(reversed(word2)))
    for i in range(length):
        if reversedWord2[i] != word1[i]:
            wasReversed = False
            break

    wasRevComp = all([False if word1[i] != reversedWord2[i] else True for i in range(length)])

    assert wasReversed == wasRevComp

    return wasReversed



def isReverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0: # and i < len(word1):
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True

print("\n\nisReverse: ")
print(isReverse("shortstop", "potstrohs"))
print(isReverse("nation", "noitan"))
print(isReverse("strawberry", "cylinder"))
print(isReverse("version", "crybaby"))

print("\n\nisReversed: ")
print(isReversed("shortstop", "potstrohs"))
print(isReversed("nation", "noitan"))
print(isReversed("strawberry", "cylinder"))
print(isReversed("version", "crybaby"))