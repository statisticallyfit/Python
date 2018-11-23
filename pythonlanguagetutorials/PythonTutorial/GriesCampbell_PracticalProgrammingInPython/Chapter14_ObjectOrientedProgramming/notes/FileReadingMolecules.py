import Molecule
import Atom


def readMolecule(readerObj):
    '''Read a single molecule from readerObj and return it or
        return None to signal EOF.'''
    line = readerObj.readline()
    if not line:
        return None

    # Name of molecule: "COMPND   name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num kind x y z"
    molecule = Molecule(name)

    while True:
        line = readerObj.readline()
        if line.startswith("END"):
            break
        key, num, kind, x, y, z = line.split()
        molecule.add(Atom(num, kind, float(x), float(y), float(z)))

    return molecule