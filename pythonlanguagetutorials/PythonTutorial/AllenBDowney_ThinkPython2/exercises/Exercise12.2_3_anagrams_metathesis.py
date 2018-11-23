
# Exercise 2: Anagrams;

def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def allAnagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def printAnagramSets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def printAnagramSetsInOrder(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filterLength(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res



#anagram_map = allAnagrams('words.txt')
#printAnagramSetsInOrder(anagram_map)

#eight_letters = filterLength(anagram_map, 8)
#printAnagramSetsInOrder(eight_letters)



# Exercise 3 - metathesis ---------------------------------------------------------------------------

def metathesisPairs(d):
    """ Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and wordDistance(word1, word2) == 2:
                    print(word1, word2)


def wordDistance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings
    returns: integer
    """
    assert len(word1) == len(word2)
    count = 0

    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count


sets = allAnagrams('words.txt')
metathesisPairs(sets)
