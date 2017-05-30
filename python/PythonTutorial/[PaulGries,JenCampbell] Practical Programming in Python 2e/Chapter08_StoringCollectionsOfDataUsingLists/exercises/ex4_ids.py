
ids = [4353, 2314, 2956, 3382, 9362, 3900]

# a
print(ids.remove(3382))
print(ids)

# b
print(ids.index(9362))

# c
ids.insert(ids.index(9362) + 1, 4499)
print(ids)

# d
ids.extend([5566, 1830])
print(ids)

# e
ids.reverse()
print(ids)

# f
ids.sort()
print(ids)