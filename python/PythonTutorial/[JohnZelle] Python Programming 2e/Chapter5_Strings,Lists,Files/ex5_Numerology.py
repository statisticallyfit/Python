import string

def nameNumber(name):
    """ Calculates the number value of a single name by summing individual
    digit values """
    lettersWithIndexes = dict(zip(string.ascii_lowercase, range(1, 27)))

    simpleName = name.lower().strip()
    nameValue = 0
    for letter in simpleName:
        if letter.isalpha():
            nameValue += lettersWithIndexes.get(letter)

    return nameValue



if __name__ == "__main__":
    print("Ashley: ", nameNumber("Ashley"))
    print("Zelle: ", nameNumber("Zelle"))
    print("Isabel: ", nameNumber("Isabel"))
    print("Dagfinn: ", nameNumber("Dagfinn"))
    print("Roxanne: ", nameNumber("Roxanne"))
    print("AnaMaria: ", nameNumber("AnaMaria"))
    print("Marina: ", nameNumber("Marina"))
    print("Aurelia: ", nameNumber("Aurelia"))
    print("Sascha: ", nameNumber("Sascha"))
    print("Danny: ", nameNumber("Danny"))
    print("Hickory: ", nameNumber("Hickory"))
    print("Neige: ", nameNumber("Neige"))
    print("Benoccio: ", nameNumber("Benoccio"))
    print("Ciprian: ", nameNumber("Ciprian"))
    print("Augustus: ", nameNumber("Augustus"))
    print("John Jacob Jingleheimer Smith: ", nameNumber("JOHN Jacob Jingleheimer Smith"))



