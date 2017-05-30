

"""
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
"""
#______________________________________________________________


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)

# declare an array that holds word lengths
word_lengths = []

# remove all "the" and add remaining word lengths to word_lengths array
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(word_lengths)


#______________________________________________________________

"""
# Declare the lists
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
poslist = []

# for each number in numbers list, check if positive
for num in numbers:
    if num > 0:
        # then add positive nums to newlist
        poslist.append(num)

# now print newlist
print(poslist)
"""