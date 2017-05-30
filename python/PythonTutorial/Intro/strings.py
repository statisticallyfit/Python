string = "Hey there! what should this string be?"

print("Warning! SPACES ARE COUNTED EVERYWHERE!!!")

# Length should be 20
print("Length of string = %d" % len(string))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % string.index("a"))

# Number of a's should be 2
print("a occurs %d times" % string.count("a"))

# Slicing the string into bits (SPACES ARE COUNTED!!!)
print("The first five characters are '%s'" % string[0:5])  # Start to 5)
print("The next five characters are '%s'" % string[5:10]) # 5 to 10
print("The twelfth character is '%s'" % string[12]) # Just number 12

print("The last five characters are '%s'" % string[-5:])  # 5th-from-last to end)

# Convert everything to uppercase
print("String in uppercase: %s" % string.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % string.lower())

# Check how a string starts
if string.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if string.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % string.split(" "))
