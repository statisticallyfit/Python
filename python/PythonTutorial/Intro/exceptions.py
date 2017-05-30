"""Exception sources"""
"""
http://www.network-theory.co.uk/docs/pytut/UserdefinedExceptions.html
http://www.tutorialspoint.com/python/python_exceptions.htm
https://docs.python.org/3.4/tutorial/errors.html#raising-exceptions
"""


"""SAMPLE USER_DEFINED EXCEPTION:"""

"""
# define Python user-defined exceptions
class Error(Exception):
   #Base class for other exceptions
   pass

class ValueTooSmallError(Error):
   #Raised when the input value is too small
   pass

class ValueTooLargeError(Error):
   #Raised when the input value is too large
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")

"""



#___________________________________________________________________



print("Please enter your full name and rank below: ")
actorName= input("name: ")
actorRank = input("rank: ")

actorNameSplit = actorName.split(" ")
print("Name:", actorNameSplit)
print("Rank: ", actorRank)

actorTotalInfo = "name: %s" % actorName + " |rank: %s" % actorRank



class Error(Exception):
   #Base class for other exceptions
   pass

class MiddleNameError(Error):
   #Raised when middle name is given
   pass

listOfSplitWords = actorTotalInfo.split(" ")

def getLastName():
    lastName = actorNameSplit[-1]
    print("List of split words: ", listOfSplitWords)
    return lastName

#if wordcount in list of split words > 5, return MiddleNameError
try:
    print("The actor's last name is %s" % getLastName())

    if len(actorNameSplit) > 2:
        raise MiddleNameError (actorNameSplit[1])

except MiddleNameError as error:
    print("There was a middle name given: ", error)
finally:
    print("Goodbye")