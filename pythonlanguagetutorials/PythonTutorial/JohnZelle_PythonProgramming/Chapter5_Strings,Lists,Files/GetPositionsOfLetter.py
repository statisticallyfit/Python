

def indexesOf(st, item):
    """Gets all indexes of the item (letter char) in string st

     Arguments:
         st = string to search in
         item = char to search for
     Returns:
          list of integers
    """
    posList = []

    while len(st) > 0:
        pos = st.find(item)
        if pos == -1:
            break

        # getting real index
        actualPos = pos
        if len(posList) > 0:
            actualPos = pos + posList[-1] + 1
        posList.append(actualPos)
        st = st[pos+1 : ] # cut out rest of string to search in

    return posList


print(indexesOf("hallelujah", "l"))
print(indexesOf("corny cupcake scoop ice cream", "c"))
print(indexesOf("banana-nation of numbthering", "n"))


# ---------------------------------------------------------------------
# another way to find indexes
def indexesOf2(word, letter):
    indexLetterPairs = enumerate(word)
    posList = []

    for pair in indexLetterPairs:
        if pair[1] == letter:
            posList.append(pair[0])
    return posList


print(indexesOf2("hallelujah", "l"))
print(indexesOf2("corny cupcake scoop ice cream", "c"))
print(indexesOf2("banana-nation of numbthering", "n"))
