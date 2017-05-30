
def histogram(str):
    d = dict()
    for char in str:
        d[char] = d.get(char, 0) + 1
    return d

hist = histogram("brontosaurus")

print("\nGETTING BRONTOSAURUS KEYS:")
# get(key, default value if key not found), else actual value of key is returned.
print(hist.get("a"))
print(hist.get("u", -99))
print(hist.get("x", -89))



def histogramGet(str):
    d = dict()
    for char in str:
        # if not there, create key and init with val zero
        # else if there then init with 1
        d[char] = d.get(char, 0) + 1
    return d

print("\n\nBETTER HISTOGRAM: ")
print(histogramGet("marble staircase \t\tthat \twra\tps around the sky"))



# 11.3 can sort dict
def dictSort(d):
    newDict = []
    for key in sorted(d):
        newDict.append((key, d.get(key)))
    return newDict

print("\nSORTED DICT: ", sorted(hist)) # acts on the KEYS only
print(dictSort(hist))




# 11.4 reverse lookup
def reverseLookup(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    raise LookupError("value does not appear in the dictionary")

print("\nREVERSE LOOKUP: ")
print(hist)
print(reverseLookup(hist, 1))
print(reverseLookup(hist, 2))
# print(reverseLookup(hist, 14))





# 11.5 inverting dictionary with lists
def invertDict(d):
    inverse = dict()
    for key in d:
        val = d.get(key)
        if val not in inverse: # if val is not a key already...
            inverse[val] = [key] # initialize with list containing key
        else:
            inverse[val].append(key)
    return inverse


print("\n\nINVERTING DICT: ", hist)
hist = histogram("parrot")
print(invertDict(hist))
print(invertDict(histogram("brontosaurus")))




# 11.6 Memoization!!

# global variable element assignment works here but if you want to reassign whole known
# dict THEN only must you declare global known in function fibonacci
known = {0:0, 1:1}
def fibonacci(n):
    global known

    if n in known:
        return known.get(n)

    result = fibonacci(n-1) + fibonacci(n-2)
    known[n] = result # adding a new result to the known list
    return result

print("\nFIBONACCI: ")
print(fibonacci(10))
print(known)



# 11.7 global variables - must declare a variable global in the local use so that computer
# recognizes it as global and doesn't create a local one with same name instead, leaving the
# global one unchanged.
beenCalled = True

def globalChange():
    global beenCalled
    beenCalled = True

count = 0
def countGlobalChange():
    global count
    count += 1