import program
import math


# assertion test
assert program.fahrenheitToCelsius(68) == 20


# function tests
epsilon = 0.00000000000000000000000000000000000000000000000001

def testCorrect():
    assert abs(program.fahrenheitToCelsius(68) - 20 < epsilon)

def testAbsoluteZero():
    try:
        program.fahrenheitToCelsius(-500)
    except AssertionError:
        pass
    else:
        # use else because: we trigger the assertion error - if it is triggered, it means we
        # tested for it in the function fahrenheitToCelsius() so that's we why let it pass.
        # However, if no assertion error is triggered we go in the 'else' block and trigger
        # another assertion to say 'absolute zero was not handled'.
        assert False,  'Absolute zero not handled'



testCorrect()
testAbsoluteZero()