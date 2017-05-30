import os



import os

def listFiles(dirName, suffix):

    for name in os.listdir(dirName):
        # note: doesn't cut it: absolutePath = os.path.abspath(name) # just simply pastes them together sometimes (see pydocs)
        absolutePath = os.path.join(dirName, name)

        if absolutePath.endswith(suffix):
            print(absolutePath)
        if os.path.isdir(absolutePath):
            listFiles(absolutePath, suffix)


testPath = "/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/COSC110/PythonSchool"
listFiles(os.getcwd(), "mp3")
print("\n\n\ntestPath:")
listFiles(testPath, "txt")