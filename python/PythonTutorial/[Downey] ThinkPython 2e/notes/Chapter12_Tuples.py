
from functools import reduce


# 12.1 tuples are immutable

t = 'a', 'b', 'c'
t1 = 'a', # tuple with single element
print(t)
print(t1)

print(type(('a')))

print(type(tuple('a')))

print(tuple("lupins"))
print(list(tuple("lupins")))
print("+".join(list(tuple("lupins"))))

t = tuple("abcd")
print(t[0], t[1])
print(t[1:3])

# error - tuples are immutable
# t[0] = 'A'
t = tuple('A') + t[1:]
print(t)

# works like decimal comparison
print((0,1,20000) < (0,3,4))
print((0,4,1) < (0, 3, 4))




# 12.2 tuple assignment
print("\nTUPLE ASSIGNMENT: ")
a = tuple("waterfall")
b = tuple("1234")
print(a, b)
a, b = b, a
print(a, b)

addr = "monty@python.org"
uname, domain = addr.split("@")
print(uname, domain)

print(divmod(7, 3))


# 12.4 variable length arg tuples

# gather
def printAll(*args): print(args)
printAll(1, 2.0, '3')

#scatter
t = (7, 3)
print(divmod(*t))



# exercise sumAll takes many args
def sum(*args):
    return reduce( (lambda x,y: x+y), args)

print(sum(1,2,3,4,5,6))





# 12.5 lists and tuples
s = "abc"
t = [0,1,2]
print(zip(s, t))
# zip obj is iterator

# can transform to list
print(list(zip(s, t)))

z = zip(s, t)
for pair in zip(s, t):
    print(pair)


# another example
print(list(zip("Anne", "Elk")))




# returns true if they match at index i
def hasMatch(tup1, tup2):
    for x, y in zip(tup1, tup2):
        if x == y:
            return True
    return False


# to traverse indices along with elements : enumerate()
for index, elem in enumerate("abcdefghij"):
    print(index, elem)

print(list(enumerate("abcdefghijklmnop")))





# 12.6: items() key-value pairs as tuple list
d = {'a':0, 'b':1, 'c':2}
print(d.items())


# can initialize dict with tuples
t = [('a', 0), ('c', 2), ('b', 1)]
print(dict(t))

# zip and dict:
d = dict(zip("abc", range(3)))
print(d)
d.update([('f', 34), ('j', 9)])
print(d)




# tuples as keys for dictionary
directory = {}
directory["Mary", "Jane"] = '416-587-3333'
directory["Angeilki", "Cosmo"] = '416-717-7777'
directory["Renata", "Bezlikova"] = "415-890-2133"
directory["Henry", "Grimm"] = "122-324-1112"
directory["Sabrina", "Grimm"] = '123-123-123'
directory["Daphne", "Grimm"] = '123-123-123'
directory["Puck", "Everafter"] = "000-000-0000"

print(directory)
for first, last in directory:
    print(first, last, ": ", directory[first, last])


# print reversing a list (reversed returns iterator)
print(list(reversed([1,2,3,4,5])))

