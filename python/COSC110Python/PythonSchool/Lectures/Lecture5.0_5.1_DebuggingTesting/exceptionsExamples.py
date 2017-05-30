
# 1: handling one exception

def example1():
    while True:
        try:
            val = input("Enter number: ")
            x = int(val)
            break
        except ValueError: # argument has right type (string) but inappropriate value (letter, should be number)
            print("Not a number!")


# example1()



# 2: handling multiple exceptions:
def toInt(val):
    try:
        result = int(val)
        print("SUCCESS")
        return result
    except TypeError:
        print("ERROR: invalid type - ", val)
    except ValueError:
        print("ERROR: not a number! - ", val)
    return 0

toInt(None)
toInt(dict())
toInt("string")
toInt("23")



# 3: grouping multiple exceptions:
def toIntGrouping(val):
    try:
        result = int(val)
        print("SUCCESS")
        return result
    except (TypeError, ValueError):
        print("ERROR: either Type or ValueError")
    return 0

print("\n\nGrouping: ")
print(toIntGrouping(None))
print(toIntGrouping("string"))
print(toIntGrouping("23"))




# 4 catchall
def toIntAll(val):
    try:
        return int(val)
    except:
        return 0
print("\n\nCatchall: ")
print(toIntAll(None))
print(toIntAll("hi"))
print(toIntAll("1"))




# 5: Else exceptions
def inverseToInt(val):
    try:
        result = int(val)
    except (TypeError, ValueError):
        print("ERROR: ", val)
        result = 0

    # NOTE: could also not use else, just use another try/except block
    else:
        try:
            result = 1/result
        except ZeroDivisionError:
            result = 0

    return result

print("\n\nInverse to int: ")
print(inverseToInt(0))
print(inverseToInt("5"))
print(inverseToInt(5))
print(inverseToInt(None))
print(inverseToInt({}))
print(inverseToInt("hi"))



# 6. Finally - gets executed regardless of error or not
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by 0!")
    else:
        print("Result is ", result)
    finally: #like releasing a file after operation on file
        print("Executing finally")

print("\n\nFinally: ")
divide(1, 0)
divide(3, 6)


# 7: raising exceptions
def divideRaise(x, y):
    if y == 0:
        raise ZeroDivisionError("y is zero: ", y)
    return x / y

print("\n\nRaise: ")
#print(divideRaise(1, 0))
print(divideRaise(4, 5))


def reraise(x, y):
    try:
        val = x / y
    except ZeroDivisionError:
        print("Logging zero division error ... ")
        # Then raise it again so you can deal with it later  in program...
        raise
    return val

print(reraise(4, 9))
# print(reraise(1, 0))






# Not in lecture: custom exception:
class CustomDivideByZeroException(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def customDivideException(x, y):
    try:
        if y == 0:
            raise CustomDivideByZeroException("zero denominator")
    except CustomDivideByZeroException as customExceptionObj:
        print("".join(customExceptionObj.args))
    else:
        return x / y
    finally:
        print("finally end")

print("\n\nCustom: ")
print(customDivideException(1, 0))
print(customDivideException(71, 123))
