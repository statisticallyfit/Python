


class HashableClass(object):
    def __init__(self, values=None, name=''):
        self.name = name
        self.d = {}

    def __key(self):
        return (self.attr_a, self.attr_b, self.attr_c)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())

    def Set(self, x, y=0):
        self.d[x] = y

    def Get(self):
        for key, val in sorted(iter(self.d.items())):
            print(key, val)

"""
dictionary = {}

# creating objects of this class
#obj = HashableClass()
dictionary['A'] = 5
dictionary['B'] = 4
dictionary['C'] = 3

for key, val in iter(dictionary.items()):
    print(key, val)

"""

#creating objects of this class
obj = HashableClass()
obj.Set(HashableClass(1), 5)
obj.Set(HashableClass(2), 4)
obj.Set(HashableClass(3), 3)

print(obj.Get())