import os



def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    names = []

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names



def computeCheckSum(filename):
    '''Computes checksum code of a file '''
    cmd = "md5sum " + filename
    return pipe(cmd)


def findDuplicates(fileList, suffix):
    codeList = []

    # computes the checksums for all the files
    d = {}
    for filename in fileList:
        if filename.endswith(suffix):
            codeMessy, _ = computeCheckSum(filename) # returns (result, status) tuple
            code, _ = codeMessy.split()

            if code in d.keys():
                d[code].append(filename)
            else:
                d[code] = [filename]

    return d


def printDuplicates(d):
    ''' Reports any duplicate files

    d: dictionary that maps between filenames and its list of duplicate files

    returns: None
    '''
    for key, duplicates in d.items():
        if len(duplicates) > 1:
            print("\nEQUIVALENT FILES:")
            for dup in duplicates:
                print(dup)



def pipe(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    result = fp.read()
    status = fp.close()
    assert status is None
    return result, status




def main():
    fileList = walk(dirname='.')
    d = findDuplicates(fileList, suffix="mp3")
    printDuplicates(d)


if __name__ == "__main__":
    main()