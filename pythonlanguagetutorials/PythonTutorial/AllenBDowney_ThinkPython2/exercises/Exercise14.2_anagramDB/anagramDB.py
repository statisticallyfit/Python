import anagramSets
import shelve
import sys

def storeAnagrams(filename, anagramMap):
    '''Returns a database from the anagramMap.

    filename: string filename of shelf.
    anagramMap: dictionary that maps strings to a list of its anagrams.
    '''
    shelf = shelve.open(filename, 'c') # mode 'c' means create it

    for word, anagrams in anagramMap.items():
        shelf[word] = anagrams

    shelf.close()


def readAnagrams(filename, wordLookup):
    '''Looks up a word in a shelf and returns list of its anagrams.

     filename: string file name of shelf (to open up persistent database)
     wordLookup: word to look up
    '''
    shelf = shelve.open(filename)
    sig = anagramSets.signature(wordLookup) # signature is word letters in order
    try:
        return shelf[sig]
    except KeyError:
        return []



def main(script, command='make_db'):
    PATH = "/datascience/projects/statisticallyfit/github/learningprogramming/Py/python/PythonTutorial/[Downey] ThinkPython 2e/exercises/"

    if command == 'make_db':
        anagramDict = anagramSets.all_anagrams(PATH + script)
        storeAnagrams('anagrams_db.txt', anagramDict)
    else:
        print(readAnagrams('anagrams_db.txt', command))


if __name__ == '__main__':
    main('words.txt')
    main('words.txt', command='pots')
