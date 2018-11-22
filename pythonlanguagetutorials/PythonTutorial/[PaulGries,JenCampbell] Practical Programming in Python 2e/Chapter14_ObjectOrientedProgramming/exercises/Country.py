

class Country:
    """A country with name, population, and area in square km."""
    def __init__(self, name, numPeople, area):
        self.name = name
        self.population = numPeople
        self.area = area

    def __repr__(self):
        return "Country({0}, {1}, {2})".format(self.name, self.population, self.area)

    def __str__(self):
        return "{0} has a population of {1} and is {2} square km.".format(self.name, self.population, self.area)

    def isLargerThan(self, other):
        return self.area > other.area

    def populationDensity(self):
        return self.population / self.area


if __name__ == "__main__":
    china = Country("China", 12309123, 234.1)
    usa = Country("USA", 313914040, 9826675)

    print(china)
    print(usa)
    print(repr(china))
    print(usa.__repr__()) # can be called both ways
    print([repr(china)])

    assert usa.isLargerThan(china)
    print(usa.populationDensity())
