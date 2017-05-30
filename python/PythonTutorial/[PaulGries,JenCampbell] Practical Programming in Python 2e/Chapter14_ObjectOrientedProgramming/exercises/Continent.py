from Country import Country
#import Country # this imports the module object - we would have to call Country.Country("Canada"...)


class Continent:
    """A continent with name and list of countries."""

    def __init__(self, name, listOfCountries):
        self.continentName = name
        self.countries = listOfCountries

    def __str__(self):
        # note: can't use join for self.countries because they aren't strings!
        result = '\n '
        for country in self.countries:
            result += str(country) + "\n "
        result = result[:-2] # taking out command and space last ones
        return self.continentName + result

    def totalPopulation(self):
        total = 0
        for country in self.countries:
            total += country.population
        return total


if __name__ == "__main__":
    canada = Country("Canada", 34482779, 9984670)
    usa = Country("United States of America", 313914040, 9826675)
    mexico = Country("Mexico", 112336538, 1943950)

    northAmerica = Continent("North America", [canada, usa, mexico])

    france = Country("France", 6681000000, 643801)
    switzerland = Country("Switzerland", 8287000000, 41285)
    italy = Country("Italy", 60800000, 301338)
    greece = Country("Greece", 1082000000, 131957)

    europe = Continent("Europe", [france, switzerland, italy, greece])

    print(northAmerica)
    print(europe)
    print(northAmerica.totalPopulation())
    print(europe.totalPopulation())
