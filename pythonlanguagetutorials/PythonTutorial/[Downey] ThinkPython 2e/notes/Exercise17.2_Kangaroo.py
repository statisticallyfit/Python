#import sys
#sys.path.append('../')
#from notes.Chapter16_ClassesAndFunctions import Time, printTime, isAfter, addTime, isEqualTime, normalize, intToTime, timeToInt, increment, isValidTime



class Kangaroo:
    """A Kangaroo is a marsupial."""

    # Default argument values are evaluated only once at function definition time, which means that
    #  modifying the default value of the argument will affect all subsequent calls of the function.
    # note: so never in conclusion put a default mutable argument as it will make changes visible to every object.
    def __init__(self, name, contents=None): # was: contents = []
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouchContents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouchContents:
            # note: could use object class's __str__() method, uncommon calling type, object.__str__(obj)
            # note - 
            s = '    ' + str(obj)
            t.append(s)
        return '\n'.join(t)

    def putInPouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouchContents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.putInPouch('wallet')
kanga.putInPouch('car keys')
kanga.putInPouch(roo)

print(kanga)
print(roo)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

# Hint: to find the problem try running pylint.