"""Dictionary sources"""
"""
http://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
"""

#declare a phonebook
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

#add Jack with his number
class Phonebook:
    def printPhonebook(self):
        for name, number in phonebook.items():
            print("%s's phone number is %d" % (name, number))

# make object of class Phonebook so we can access function
phone1 = Phonebook()

print("\n\nPhonebook before changes:")
phone1.printPhonebook()

# add Jake and remove Jill
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

print("\n\nPhonebook after changes:")
phone1.printPhonebook()
#or --> del phonebook["John"]
