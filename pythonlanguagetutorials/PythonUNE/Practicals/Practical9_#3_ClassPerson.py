

class Person:
    """A person with attributes name (str), age (int) in years. """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{0} is {1} years old.".format(self.name.capitalize(), self.age)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, newName):
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge

    def isOlderThan(self, other):
        return self.age > other.age




if __name__ == "__main__":
    harry = Person("Harry", 12)
    liza = Person("Liza", 13)
    jane = Person("Jane", 10)
    caroline = Person("Caroline", 12)

    assert not harry.isOlderThan(caroline)
    assert not harry.isOlderThan(liza)
    assert not caroline.isOlderThan(harry)
    assert liza.isOlderThan(harry)

    assert liza.isOlderThan(jane)
    assert not jane.isOlderThan(harry)
    assert caroline.isOlderThan(jane)

    print("{0}\n{1}\n{2}\n{3}".format(harry, liza, jane, caroline))
