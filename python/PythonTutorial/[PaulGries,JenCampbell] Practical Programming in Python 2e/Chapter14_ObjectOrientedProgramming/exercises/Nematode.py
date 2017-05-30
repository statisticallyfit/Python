

class Nematode:
    """A nematode type of C.elegans, with body length, gender, and age."""
    def __init__(self, length, isMale, age):
        self.bodyLength = length
        self.gender = "male" if isMale else "hermaphrodite"
        self.daysOld = age

    def __str__(self):
        return "C.elegans: {0} millimeters long, {1} gender, {2} days old."\
            .format(self.bodyLength, self.gender, self.daysOld)

    '''
    def __repr__(self):
        return "Nematode(bodyLength={0}, gender={1}, daysOld={2})"\
            .format(self.bodyLength, self.gender, self.daysOld)

    '''


if __name__ == "__main__":
    nematodeMale = Nematode(5, True, 8)
    nematodeFemale = Nematode(4, False, 9)
    print(nematodeMale)
    print(nematodeFemale)
    print(repr(nematodeMale))
    print(repr(nematodeFemale))
