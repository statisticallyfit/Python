

# FORMAT SEQUENCE has the following components (in order):
print("\n\nFORMAT OPERATORS: -------------------------------- \n")

# % = start of format
# optional mapping key
# optional conversion flags
# optional field width
# optional . followed by precision
# optional length modifier
# conversion type

# Format operator = %
print("Hello %s. %d/2 is %g" % ("Fred", 5, 5/2))

# Mapping key - allows dict lookup
print("%(unit)s has %(students)d students and %(cobbles)g cobbles" %
      {'unit':"COSC110", 'students':100, 'cobbles':19.43})


# conversion flag
# %0+5g = zero pad, plus in front, all 5 chars long
print("%0+5g %0+5g" % (1, -1)) # minus replaced plus

print("%E" % 1.1)
print("%e" % 0.00011)
print("%f" % 0.0001) # extra decimals
print("%F" % 0.0001) # extra decimals
# %g chooses between e and f (optimizes best presentation)

print("You scored %d%%!" % 100) # missing arg space filled by second % after d's %

# field width
# todo
# . followed by precision
# todo





# Files and Directories
print("\n\nFILES AND DIRECTORIES: -------------------------------- \n")

import os

cwd = os.getcwd()
print(cwd)

print(os.path.abspath("Lecture6.0.py"))
print(os.path.abspath("Lectures"))
print(os.path.exists("Lectures/"))

print(os.path.isfile("Lecture6.0.py"))
print(os.path.isdir("Lecture6.0.py"))

print(os.listdir(cwd)) # gets list of filenames and directories in the current directory.

print(os.path.join(cwd, "extraFilename.txt"))







# Reading FIle
print("\n\nREADING FILE: -------------------------------- \n")

fileIn = open("report.txt")
for line in fileIn:
    word = line.strip()
    print(word)
fileIn.close() # problems if don't close if someone is using it at the same time.


# no need to close manually - closes file automatically once leaving block:
with open("report.txt") as fileIn:
    for line in fileIn:
        print(line.strip())
print("File now closed")




# WRITING TO FIle
print("\n\nWRITING FILE: -------------------------------- \n")

# overwriting a file
fileOut = open("report.txt", "w") # "r" is default value to read, "a" means append liens
print(fileOut.write("Hello, world!\n"))
print(fileOut.write("This is a simple text file"))
print(fileOut.write(" that I created!\n"))
print(fileOut.write("Goodbye."))
fileOut.write("\nA number: %d/%d/%d" % (4, 23, 1997))
fileOut.close()