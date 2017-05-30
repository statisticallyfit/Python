

import os

def walk(dirName):
    for name in os.listdir(dirName):
        path = os.path.join(dirName, name) # the absolute path

        if os.path.isdir(path):
            walk(path)
        else:
            print(path)

# Current path
print("\nCurrent path:")
walk(os.getcwd())

print("\nTest path:")
testPath = "/datascience/projects/statisticallyfit/github/learningprogramming/Python/python/COSC110Python/PythonSchool/Lectures"
walk(testPath)
