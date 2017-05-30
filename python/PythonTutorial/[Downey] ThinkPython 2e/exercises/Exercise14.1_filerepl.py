 # the 'sed' function
'''
def copyFileReplaceText(patternStr, replaceStr, fromFilename, toFilename):
    tryIt(open, fromFilename, "Error in opening FROM file")
    tryIt(open, toFilename, "Error in opening TO file")

    fromFile = open(fromFilename)
    # get content from the file
    toFile = open(toFilename, 'w') # creates file, if exists it clears it.

    for line in fromFile:
        if patternStr in line:
            first, second = line.split(patternStr)
            tryIt(toFile, write, first + replaceStr + second, "Error in writing to file")
        tryIt(toFile.write(line), "Error in writing to file")

    tryIt(fromFile.close(), "Error in closing file")
    tryIt(toFile.close(), "Error in closing file")

# for object methods
def tryIt(obj, f, arg, message):
    try:
        obj.f(arg)
    except:
        print(message)

def tryIt(f, arg, message):
    try:
        f(arg)
    except:
        print(message)
'''

def copyFileReplaceText(patternStr, replaceStr, fromFilename, toFilename):
    fromFile = open(fromFilename, 'r') # read mode
    toFile = open(toFilename, 'w') # creates file, if exists it clears it.

    for line in fromFile:
        if patternStr in line:
            first, second = line.split(patternStr)
            toFile.write(first + replaceStr + second)
        else:
            toFile.write(line)

    fromFile.close()
    toFile.close()


if __name__ == "__main__":
    PATH = "/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/"
    print(copyFileReplaceText("butterfly", "bird", "temp.txt", "newTemp.txt"))
    copyFileReplaceText("buttermilk", "golden", "temp.txt", "newTemp2.txt")
    copyFileReplaceText("tulip", "daisy", "newTemp2.txt", "newTemp3.txt")