
class Point:
    """A point in 3D space."""
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)


class Atom:
    """An atom with number, symbol, coordinates."""
    def __init__(self, num, sym, point):
        self.number = num
        self.center = point
        self.symbol = sym

    def __str__(self):
        return "({0}, {1})".format(self.symbol, self.center)

    # note: printing the id or number for debugging purposes in repr.
    def __repr__(self):
        return "Atom(number={0}, sym={1}, center={2})".format(self.number, self.symbol. self.center)

    def translate(self, deltaPoint):
        # moving this atom by adding the deltaPoint to atom's center.
        self.center = (self.center.x + deltaPoint.x,
                       self.center.y + deltaPoint.y,
                       self.center.z + deltaPoint.z)




class Molecule:
    """A molecule with a name and list of Atoms. """
    def __init__(self, name):
        self.name = name
        self.atoms = []

    # note: can't use join() because args must be strings
    def __str__(self):
        res = '\n  '
        for atom in self.atoms:
            res += str(atom) + "\n  "
        res = res[:-2] # strip off last comma and space
        return "({0}, {1})".format(self.name, res)


    def __repr__(self):
        res = ''
        for atom in self.atoms:
            res += repr(atom) + ", "
        res = res[:-2] # strip off last comma and space
        return 'Molecule("name={0}", atoms=({1}))'.format(self.name, res)

    def add(self, anAtom):
        # Add atom to my list of Atoms
        self.atoms.append(anAtom)

    def translate(self, deltaPoint):
        for atom in self.atoms:
            atom.translate(deltaPoint)



# some test code
if __name__ == "__main__":
    ammonia = Molecule("AMMONIA")
    ammonia.add(Atom(1, "N", Point(0.257, -0.363, 0.0)))
    ammonia.add(Atom(2, "H", Point(0.257, 0.727, 0.0)))
    ammonia.add(Atom(3, "H", Point(0.771, -0.727, 0.899)))
    ammonia.add(Atom(4, "H", Point(0.771, -0.727, -0.890)))
    ammonia.translate(Point(0, 0, 0.2)) # up by 0.2 units

    print(ammonia)