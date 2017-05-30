import routes

'''

def erasePrevRoutes():
    routes.ROUTE_RECORD = []
    print(routes.ROUTE_RECORD)


'''


# ----------------------------------------- Part 1: input validation -----------------------------------------

def testValidInput():
    # note: not valid any longer since we can't have space after comma.
    # simple cases
    assert not routes.isValidInput(123)
    assert not routes.isValidInput("hello")
    assert not routes.isValidInput("123")
    assert not routes.isValidInput("1,, ")
    assert not routes.isValidInput("")
    assert not routes.isValidInput(" ")

    # good ratio
    assert not routes.isValidInput("123, 0.00")
    assert routes.isValidInput("121,0.00")
    assert not routes.isValidInput("1, 0.00")
    assert routes.isValidInput("11,0.00")
    assert not routes.isValidInput("  12, 0.00 ")
    assert routes.isValidInput("14,0.00")
    assert not routes.isValidInput("0, 0.00")
    assert routes.isValidInput("10,0.00")
    assert not routes.isValidInput("11.234, 0.00")
    assert not routes.isValidInput("11.234,0.00")
    assert not routes.isValidInput("-123, 0.00")
    assert not routes.isValidInput("-123,0.00")
    assert not routes.isValidInput("-123, -0.00")
    assert not routes.isValidInput("-123,-0.00")

    # bad ratio
    assert not routes.isValidInput("125, 1.12")
    assert routes.isValidInput("127,6.83")
    assert not routes.isValidInput("1, 4.442")
    assert not routes.isValidInput("19,4.442")
    assert not routes.isValidInput("2, 00000.00")
    assert routes.isValidInput("3,00000.00")
    assert not routes.isValidInput("7, 9.99")
    assert routes.isValidInput("8,9.99")
    assert not routes.isValidInput("11.234, 1.11")
    assert not routes.isValidInput("11.234,2.15")
    assert not routes.isValidInput("-123, 1.00")
    assert not routes.isValidInput("-123,23.009")
    assert not routes.isValidInput("-123, -1.11")
    assert not routes.isValidInput("-123,-1.45")



def testValidRatio():
    # simple cases
    assert not routes.isValidRatio(0)
    assert not routes.isValidRatio(120.12)
    assert not routes.isValidRatio(120)
    # actual cases
    assert routes.isValidRatio("123.12")
    assert routes.isValidRatio("123.00")
    assert routes.isValidRatio("123.11")
    assert routes.isValidRatio("123.44")
    assert routes.isValidRatio("00.1") # leave this to pass because not specified in instructions.
    assert not routes.isValidRatio(".")
    assert routes.isValidRatio(".12")
    assert not routes.isValidRatio(".1")
    assert not routes.isValidRatio(".111")


def testValidRoute():
    # simple cases
    assert not routes.isValidRoute(234)
    assert not routes.isValidRoute("holly")
    assert not routes.isValidRoute(",")

    # actual cases
    assert routes.isValidRoute("234")
    assert routes.isValidRoute("1231239823498234")
    assert not routes.isValidRoute("1231239823498234qwertuyiop234")
    assert not routes.isValidRoute("234.1")
    assert not routes.isValidRoute("234.0")
    assert not routes.isValidRoute("234.")
    assert not routes.isValidRoute("0.0")
    assert not routes.isValidRoute("0")



def testUniqueRoute():
    # simple cases
    assert not routes.isUniqueRoute("12")
    assert not routes.isUniqueRoute("hello2you")

    # actual cases
    assert not routes.isUniqueRoute(123, prevRoutes=[123, 456, 12, 111])
    assert routes.isUniqueRoute(123, prevRoutes=[122, 456, 12, 111])
    assert not routes.isUniqueRoute(123, prevRoutes=[121, 456, 12, 111, 123])
    assert not routes.isUniqueRoute(123, prevRoutes=[123, 456, 123, 12, 111])
    assert not routes.isUniqueRoute(123, prevRoutes=[56, 123, 12, 111, 123])
    assert not routes.isUniqueRoute(123, prevRoutes=[144, 456, 123, 12, 111])


# TODO: note tests are invalid because parameters have changed...
'''
if __name__ == "__main__":
    testRoute.testValidInput()
    testRoute.testValidRatio()
    testRoute.testValidRoute()
    testRoute.testUniqueRoute()
'''



# ------------------------------------------- Part 2: Reading Input -------------------------------------------

# -------------------------------------- Part 3: Sorting Data Structure --------------------------------------
