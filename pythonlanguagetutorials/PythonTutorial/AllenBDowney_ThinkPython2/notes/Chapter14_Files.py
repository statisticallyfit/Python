PATH = "/datascience/projects/statisticallyfit/github/learningprogramming/Python/python/PythonTutorial/[Downey] ThinkPython 2e/notes/"
PATH_TUTORIAL = "/datascience/projects/statisticallyfit/github/learningprogramming/Python/python/PythonTutorial/"

# 14.2 - reading/writing files
# note: careful with the 'w' option - if file exists, it gets cleared.
fout = open(PATH + 'output.txt', 'w')
line1 = "This here's the wattle,\n"
print(fout.write(line1)) # num chars added
line2 = "the emblem of our proud land.\n"
print(fout.write(line2))


# 14.3 - FORMAT OPERATORS

print("In %d years I have spotted %g %s" % (3, 0.1, "camels"))



# 14.4 - FILENAMES AND PATHS:
import os
currentWorkingDirectory = os.getcwd()
print("current working directory: ", currentWorkingDirectory)

# getting the absolute path:
print("Absolute path: ", os.path.abspath("Chapter12_Tuples.py"))
print("Absolute path: ", os.path.abspath("exercises"))

# check existence:
print("exists?: ", os.path.exists("memo.txt"))
print("exists?: ", os.path.exists("/home/statisticallyfit/COSC110")) # note: need to give full path for directories to check existence
print("exists?: ", os.path.exists("Chapter8_Strings.py"))

# check if directory:
print("is dir?: ", os.path.isdir("memo.txt"))
print("is dir?: ", os.path.isdir("/home/statisticallyfit/COSC110"))
print("is dir?: ", os.path.isdir("Chapter14_Files.py"))

# check if file:
print("is file?: ", os.path.isfile("memo.txt"))
print("is file?: ", os.path.isfile("/home/statisticallyfit/COSC110"))
print("is file?: ", os.path.isfile("Chapter14_Files.py"))

# listing directories (and files too!) note
print("all directories: ", os.listdir(currentWorkingDirectory))


# printing directories recursively
def walk(dirName):
    for name in os.listdir(dirName):
        path = os.path.join(dirName, name) # joining dir and name

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# note: only os.listdir and os.walk do not call the os.path package.
def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the exercise solution, which uses os.walk.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


#print("\n\nwalk 1: ")
#walk('/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial')
#print("\nwalk2: ")
#walk2(PATH_TUTORIAL)




# 14.5 -- catching exceptions
# note: better to go ahead and open the file rather than check all
# conditions (exists, isfile) because code is time-consuming.
print("\n\nOpening a bad file: ")
try:
    fin = open('bad-file')
except:
    print('Something went wrong.')





# 14.6 - database and persistence
import dbm

# note keys and items must be strings or bytes - others will give error.

print("\n\nDatabases:\n")
# creating database named captions, mode 'c' means create if doesn't already exist.
db = dbm.open('captions.txt', 'c')
db['cleese.png'] = 'Photo of John Cleese.'
print(db['cleese.png'])

db['cleese.png'] = 'Photo of John Cleese doing a silly walk.' # replacing
print(db['cleese.png'])

#iteration: no dict stuff like keys, items, so use for-loop:
# note .. ? it works ?
print("\n")
for key in db.keys():
    print("key: ", key, ";  item: ", db[key])

# should close when done
db.close()





# 14.7 - pickling allows conversion of objects

# note: translates any object into string suitable for database storage then translates
# the string back to objects

import pickle

t1 = [1,2,3]
s = pickle.dumps(t1) # return string representation
t2 = pickle.loads(s) # convert back to object
print("\n\n")
print(s)
print(t2)

print("\nSame effect as copying: ")
print(t1 == t2) # same content
print(t1 is t2) # not in general the same object







# 14.8 - Pipes: any program you can launch from shell can be launched from Python
# using a pipe object, which represents a running program.
cmd = 'ls -l'
fp = os.popen(cmd) # behaves like file:
result = fp.read() # get whole thing at once, or use readline()
print(result)
status = fp.close()
print(status) # None means it ended with no errors

# using command md5sum to check if two files have same content.
filename = 'output.txt'
filename2 = 'captions.txt'
cmd = "md5sum " + filename + " " + filename2
fp = os.popen(cmd)
result1 = fp.read()
status1 = fp.close()
print(result1)
print(status1)





# 14.9 - writing modules
import wc

print(wc.lineCount('wc.py'))








# 14.10 - debugging

# repr() returns string exact representation (what's inside)
s = '1 2 \t\t\t 3 \n 4'
print(s)
print(repr(s))

# filtering out all tab chars
newS = ''
for char in s:
    if char != "\t":
        newS += char
print(newS)