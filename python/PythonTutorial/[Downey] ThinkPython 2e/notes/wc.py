def lineCount(filename):
    count = 0
    for line in open(filename): # open(filename) returns array
        count += 1
    return count

# the test code that gets printed if we import and don't use __main__
#print(lineCount('wc.py'))

# note: putting the testcode in name main check stops it from being run when imported because
# the file you import it in will have the name main while this file will have name wc so the check
# will be false (happens only when you run this module from the other "main" one)
if __name__ == '__main__':
    print(lineCount('wc.py'))