
print("Hello, world!")

print("I am " + str(20+80) + " years old")


counter = 100     # integer
miles = 1000.0    # floating point
name = "Isabel DaSilva"   # string

print(counter, miles, name)

"""

ATTEMPT AT EXCEPTION HANDLING:

integer = 1
obj = "greeting"

print("Here is your integer and object: " + str(integer) + " and " + obj)
print("... and now we delete them: ")


try
    del integer, obj
    print("Not here?" + str(integer) + " and " + obj)
except DeleteError:
    print("Variables were deleted")
"""


#____________________________________________________________________________________________-

#variables demonstrated
print("\n\n\n\nThis program is a demo of variables")
v = 1
print("The value of v is now", v)
v = v + 1
print("v now equals itself plus one, making it worth", v)
v = 51
print("v can store any numerical value, to be used elsewhere.")
print("for example, in a sentence. v is now worth", v)
print("v times 5 equals", v * 5)
print("but v still only remains", v)
print("to make v five times bigger, you would have to type v = v * 5")
v = v * 5
print("there you go, now v equals", v, "and not", v / 5)


print("\n\n\nNow STRINGS: ")
snippet1 = "The bird"
snippet2 = " sat "
snippet3 = "on the cherry tree"

sentence = snippet1 + snippet2 + snippet3
print(sentence)
