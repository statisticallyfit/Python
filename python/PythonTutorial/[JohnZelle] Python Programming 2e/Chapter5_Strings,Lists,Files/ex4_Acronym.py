

def createAcronym(phrase):
    """Converts a phrase into an acronym
    """
    titleCaseWords = phrase.title().split(" ")
    acronym = ""

    for word in titleCaseWords:
        if word.isalpha():
            acronym += word[0]
    return acronym


print(createAcronym("random access memory"))
print(createAcronym("the cow jumped over the moon"))
print(createAcronym("mothers against drunk driving"))
print(createAcronym("fairy god mothers against drunk driving"))
print(createAcronym("Keep  it -- simple silly"))