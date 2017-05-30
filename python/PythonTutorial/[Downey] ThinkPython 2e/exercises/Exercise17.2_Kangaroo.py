class Kangaroo:
    """A Kangaroo is a marsupial."""

    #Default argument value is mutable less.
    # This inspection detects when a mutable value as list or dictionary is detected in a
    # default value for an argument. Default argument values are evaluated only once at
    # function definition time, which means that modifying the default value of the argument
    # will affect all subsequent calls of the function.
    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents



    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + str(obj) # can use this instead of: object.__str__(obj)
            # note: object.__str__(obj) is the old naming like Time.add(start, t1)
            t.append(s)
        return '\n'.join(t)

    def putInPouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.putInPouch('wallet')
kanga.putInPouch('car keys')
kanga.putInPouch(roo)

print(kanga)
print(roo)