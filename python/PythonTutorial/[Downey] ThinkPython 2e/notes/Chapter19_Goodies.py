import math


# 19.1 -- Conditional expressions

# example 1
x = 10
y = math.log(x) if x > 0 else float('nan') # instead of straight-up if-else

# example 2
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# example 3: handling optional arguments
def initialize_bad(self, name, contents=None):
    self.name = name
    if contents == None:
        contents = []
    self.pouchContents = contents

def intialize_good(self, name, contents=None):
    self.name = name
    self.pouchContents = [] if contents == None else contents





# 19.2 -- list comprehensions:
def capitalizeAll_bad(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalizeAll_good(t):
    return [s.capitalize() for s in t]



def onlyUpper_bad(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def onlyUpper_good(t):
    return [s for s in t if s.isupper()]





# 19.3 - generator expressions (similar to list comprehensions except for parantheses
# instead of square brackets)
g = (x**2 for x in range(5))
print(g)
#print(next(g))
#print(next(g))
#print(next(g))
for val in g:
    print(val)




# 19.4 -- any and all
print(any([False, False, True]))
print(any(letter == 't' for letter in 'monty'))

def avoids(word, forbidden):
    # word avoids forbidden if there are NOT any forbidden letters in word
    return not any(letter in forbidden for letter in word) # note: generator expr.

# note: more efficient to use generator because it stops immediately if it finds True.
print(avoids("peaches", "diff"))
print(avoids("peaches", "summer rain"))




# 19.5 -- sets

# note: d1 contains words from document as keys and d2 contains list of words
# Returning a dictionary containing keys from d1 that are not in d2.
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res
# note: inefficient because some values are None (never used). Set is more efficient

# note: set behaves like collection of dictionary keys with no values. Contains no duplicates.
def subtract_good(d1, d2):
    return set(d1) - set(d2)




# note: when element appears for the first time, it is added. If same element
# appears again, then it is duplicated so return True right away.
def hasDuplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def hasDuplicates_good(t):
    return len(set(t)) < len(t)




# note: checks whether all letters in word are in available.
def usesOnly(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def usesOnly_good(word, available):
    return set(word) <= set(available) # no duplicates, so len is the only variable






# note: rewrite avoids using sets: intersection is 0
def avoidsWithSets(word, forbidden):
    return (set(word) & set(forbidden)) == set()

def avoidsDisjoint(word, forbidden):
    return word.isdisjoint(forbidden)

print("avoids with sets: ", avoidsWithSets("peaches", "diff"))
print("avoids with sets: ", avoidsWithSets("peaches", "summer rain"))
print("avoids disjoint: ", avoidsWithSets("peaches", "diff"))
print("avoids disjoint: ", avoidsWithSets("peaches", "summer rain"))



print("\n\nsets: ")
peaches = set("peaches")
summerrain = set("summer rain")
manyrains = set("many summer rains")
diff = set("diff")
print("isdisjoint: ", peaches.isdisjoint(summerrain), peaches.isdisjoint(diff)) # intersect is zero
print("issubset: ", peaches.issubset(summerrain), summerrain.issubset(manyrains)) # <=
print("issuperset: ", manyrains.issuperset(summerrain)) # >=
print("intersection: ", peaches.intersection(diff), summerrain.intersection(peaches), peaches.intersection(summerrain)) # &
print("union: ", peaches.union(diff), peaches.union(summerrain), summerrain.union(manyrains)) # set | other | ...
# new set with elements in this set that are not in the others.
print("difference: ", peaches.difference(diff), peaches.difference(summerrain), summerrain.difference(peaches)) # set - other - ...
# new set with elements in either set that are not in both
print("symmetric difference: ", peaches.symmetric_difference(diff))








# 19.6 - Counters
# note: counters are like multisets: say how many times each element appears

from collections import Counter

count = Counter("Mississippi") # note must pass in anything that supports iteration + is hashable.
print("\n\n", count)
print(count['d']) # note: no exception, just 0
print(count['m']) # case sensitive


# print: return the 3 most common:
print(count.most_common(3))
print(count.most_common())
print(count)
print(count.most_common(0))
print("count.elements(): ", count.elements())
print("sorted(count): ", sorted(count)) # capitals come first

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print("\nafter subtracting: ")
c.subtract(d)
print(c)
print(d)
print("\nafter updating:")
c.update(Counter(a=10, r=5, u=3, v=0, c=-1))
d.update(Counter(c=1, r = 4))
print("c: ", c)
print("d: ", d)
print("\nadding: ", c + d) # note keeps only positive counts (> 0)
print("subtracting: ", c - d) # note keeps only positive counts (> 0)
print("intersection: ", c & d) # note: min of c and d elements
print("union: ", c | d) # note: max of c and d elements
print("\nunary: ")
print("c: ", c, "\n+c: ", +c) # keeps positives only, no zeroes either
print("c: ", c, "\n-c: ", -c) # keeps negatives only, absolute value, no zeroes either.



# note: If two words are anagramss, they contain same letters with same counts
def isAnagram(word1, word2):
    return Counter(word1) == Counter(word2)








# 19.7 - defaultdict

from collections import defaultdict
d = defaultdict(list)# note: arg is list class object used as factory to create objects.
t = d['new key'] # accessing nonexistent key makes it.
print("\nDEFAULT DICT: ", t)
t.append('new value')
print(d)




'''
def allAnagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        sig = signature(word)
        if sig not in d:
            d[sig] = word
        else:
            d[sig].append(word)
    return d


def allAnagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        sig = signature(word)
        d.setdefault(sig, []).append(word)
    return d
'''







# 19.8 -- named tuples

from collections import namedtuple

# first arg = name of class to create; the secondarg = list of attributes Point objects should have as strings.
# return value is an object
print("\n\nNamed tuples: ")
Point = namedtuple('Point', ['x', 'y'])
print(type(Point))
p = Point(1, 2)
print(p, p.x, p.y)

# can treat it as a tuple
print(p[0], p[1])
x, y = p
print(x, y)






# 19.9 - gathering keyword args
def printAll_nokeyword(*args):
    print(args)

def printAll_gatherskeywords(*args, **kwargs):
    print(args, kwargs)

print("\n\nGathering keyword args: ")
# printAll_nokeyword(1, 2.0, third='3') note error
printAll_gatherskeywords(1, 2.0, third='3')



# scattering dict to get assigned to y as well
d = dict(x=1, y=2)
print(Point(**d))
# print(Point(d)) note error