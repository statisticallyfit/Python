
def dutchFlagIntuitive(colors):
    numRed, numGreen, numBlue = 0, 0, 0
    for col in colors:
        if col == "red":
            numRed += 1
        elif col == "green":
            numGreen += 1
        else:
            numBlue += 1

    newColors = []
    newColors.extend(("red\n" * numRed).split())
    newColors.extend(("green\n" * numGreen).split())
    newColors.extend(("blue\n" * numBlue).split())
    return newColors


def dutchFlag(colors):
    '''Return colors rearranged so that 'red' strings come first, then 'green', then 'blue'.
    :param colors: list of string colors, red, green, blue
    :return: rearranged colors list
    '''

    startGreen = 0 # index of green section start
    startUnknown = 0 # index of first unexamined color.
    endUnknown = len(colors) - 1 # index of first unexamined color

    while startUnknown <= endUnknown:
        # if red, swap it with item to the right of the red section
        if colors[startUnknown] == "red":
            colors[startGreen], colors[startUnknown] = colors[startUnknown], colors[startGreen]
            startGreen += 1
            startUnknown += 1
        # else if green leave it where it is
        elif colors[startUnknown] == "green":
            startUnknown += 1

        # else if blue, swap it with item to the left of the blue section
        else:
            colors[startUnknown], colors[endUnknown] = colors[endUnknown], colors[startUnknown]
            endUnknown -= 1



if __name__ == "__main__":
    colors = ['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green', 'red', 'blue', 'blue', 'green', 'blue',
              'green']
    print(colors)
    dutchFlag(colors)
    print(colors)

    print(dutchFlagIntuitive(colors))
