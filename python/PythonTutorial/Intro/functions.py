
"""

def list_benefits():
	return [ "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"];


def build_sentence(info):
    return info + " is a benefit of functions!"

#calling
#print(list_benefits())
print(build_sentence(list_benefits()[0]))
print(build_sentence(list_benefits()[1]))
print(build_sentence(list_benefits()[2]))
Process finished with exit code 0

"""

# _________________________________________________________________________________

"""
# Modify this function to return a list of strings as defined above
list_of_benefits = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"];

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(info):
    return info + "is a benefit of functions!"

def name_the_benefits_of_functions():
    #list_of_benefits = list_benefits()
    for info in list_of_benefits:
        print(build_sentence(info))


name_the_benefits_of_functions()

"""




""" EXCEPTION ERROR TO FIX:

Connected to pydev debugger (build 135.1057)
More organized codeis a benefit of functions!
More readable codeis a benefit of functions!
Easier code reuseis a benefit of functions!
Allowing programmers to share and connect code togetheris a benefit of functions!
Traceback (most recent call last):
Exception ignored in: <function WeakSet.__init__.<locals>._remove at 0x0000000002324EA0>
Traceback (most recent call last):
  File "C:\D\bin\Anaconda3\lib\_weakrefset.py", line 38, in _remove
  File "C:\D\bin\JetBrains\PyCharm 3.4.1\helpers\pydev\pydevd.py", line 1087, in trace_dispatch
  File "C:\D\bin\Anaconda3\lib\traceback.py", line 252, in print_exc
  File "C:\D\bin\Anaconda3\lib\traceback.py", line 169, in print_exception
  File "C:\D\bin\Anaconda3\lib\traceback.py", line 153, in _format_exception_iter
  File "C:\D\bin\Anaconda3\lib\traceback.py", line 79, in _extract_tb_iter
TypeError: 'NoneType' object is not callable

Process finished with exit code 0

"""
#_________________________________________________________________________________
"""
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5, 6, 7, 8, 1001, 1232, 1997, 345, 12, "baby")
"""

#_________________________________________________________________________________
"""
def function(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first

result = function(1, 2, 3, action = "sum", number = "first")
print("Result: %d" % result)
"""

#_________________________________________________________________________________


magicnumber = None

# edit the functions prototype and implementation
def foo(a, b, c, *restOfArgs1):
    return restOfArgs1

def bar(a, b, c, *restOfArgs2):
    if magicnumber == 7:
        return "True"
    else:
        return "False"


# code
magicnumber = 7

print(foo(1, 2, 3, magicnumber))
print(bar(1, 2, 3, magicnumber))

