


def rightJustify(aString):
    numSpaces = 70 - len(aString)
    result = aString

    # if numSpaces is 0 or negative, we don't add any space (automatic range behavior)
    for s in range(numSpaces): # 0 ... numspace-1
        result = " " + result

    print(result)


# add spaces to front until the entire string is 70 characters long
# NOTE: if 70 - len is negative (astring len > 70) then  the overall string
# becaomse length zero! So no space is added to aString.
def rightJustifyFunctional(aString):
    print(" " * (4 - len(aString)) + aString)


rightJustify("monty")
rightJustify('monty') # whew so adding 'monty' type string to " " type string doesn't cause error!
rightJustify("banana tree")
rightJustify("3")
rightJustify("clover is cool and dewy")