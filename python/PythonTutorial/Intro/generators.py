"""
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1,40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print("And the next number is... %d!" % random_number)
"""




"""______________________________________________________"""



"""
Write a generator function which returns the Fibonacci series.
They are calculated using the following formula:
The first two numbers of the series is always equal to 1,
and each consecutive number returned is the sum of the last two numbers.
Hint: Can you use only two variables in the generator function?
Remember that assignments can be done simultaneously.
The code

a = 1
b = 2
a, b = b, a

will simultaneously switch the values of a and b.



# fill in this function
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# make loop to print fibonacci numbers
for n in range(1, 30):
    print(fib(n))
"""



# testing code
"""import types
n = 1
if type(fib(n)) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

"""
#____________________________________________________________________

def staticnum():
    k = 0
    while True:
       k += 1
       yield k
static = staticnum().__next__
for i in range(0,10):
    print(static())
