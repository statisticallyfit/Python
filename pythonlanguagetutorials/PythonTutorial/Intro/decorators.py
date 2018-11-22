"""@decorator"""
""" Decorator = function which takes several functions and returns one only. """

""" #See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works"""

"""
#repeater
@repeater
def multiply(num1, num2):
    print(num1 * num2)


# function call
multiply(2, 3)
"""
"""
def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2*old_function(*args, **kwds) #modify the return value
    return new_function
"""


#____________________________________________________________________

"""
# modeling the Double_Out function
# CHANGE OUTPUT
def doubleOut(divide):
    # multiply is new function, divide is old function
    def multiply(num1, num2):
        return 2*divide(num1, num2) # to modify the return value
    return multiply(30,6)
    # returns new function

def divide(num1, num2):
    return num1/num2

print(doubleOut(divide))
"""

#____________________________________________________________________

# CHANGE INPUT
"""
def Double_In(old_function):
    def new_function(arg): #only works if the old function has one argument
        return old_function(arg*2) #modify the argument passed
    return new_function


def doubleIn(divideByTwo):
    def multiply(num): #only works if divide, which is old function, has one argument.
        return divideByTwo(num * 3) # modifying argument passed.
    return multiply(8)

def divideByTwo(num):
    return num/2


result = doubleIn(divideByTwo)
print("The result is: %d" % result)

"""
#____________________________________________________________________

# CHECKING

# define the checking function
def errorCheck(divideByTwo):
    def multiply(num):
        if num < 0:
            raise (ValueError, "Negative Argument")
        divideByTwo(-2)
    return multiply(-1)


# define the divide function
def divideByTwo(num):
    return num/2

# define try/catch block
try:
    answer = errorCheck(divideByTwo(-2))
    print(answer)
except ValueError:
    errorCheck(divideByTwo(-2))
finally:
    print("Program over")