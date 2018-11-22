class Hero:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return self.name + self.lastname + str(self.age)

    def __key(self):
        return (self.name, self.lastname, self.age)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        print(hash(str(self)))
        return hash(str(self))

heroes = set()

hero1 = Hero('Zina', 'Portnova', 16)
heroes.add(hero1) # gets hash -8926039986155829407
print(len(heroes)) # gets 1

hero2 = Hero('Lara', 'Miheenko', 17)
heroes.add(hero2) # gets hash -2822451113328084695
print(len(heroes)) # gets 2

hero3 = Hero('Lara', 'Miheenko', 19)
heroes.add(hero3) # gets hash -2822451113328084695
print(len(heroes)) # gets 3

hero4 = Hero('Zina', 'Portnova', 16)
heroes.add(hero4) # gets hash -8926039986155829407
print(len(heroes)) # gets 3!

"""
herosdict = dict()

herosdict[hero1.__key()] = hero1
herosdict[hero2.__key()] = hero2
herosdict[hero3.__key()] = hero3
herosdict[hero4.__key()] = hero4
"""