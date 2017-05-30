
# want to compare countdown's recursion to factorial recursion:
# for both, debugger does whiplash (as frames go back to oldest ones)
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)


def factorial(n):
    space = ' '* (4*n)
    print(space, 'factorial', n)

    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        result = n * factorial(n-1)
        print(space, 'returning', result)
        return result


def fibonacci(n):
    if not isinstance(n, int):
        print("Factorial only defined for integers.")
        return None
    elif n < 0:
        print("Factorial only defined for positive integers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print("n = ", n, "|  fib(n-1) + fib(n-2) = ", result)
        return result


print("FACTORIAL: ")
print(factorial(3))
print(factorial(5))
print(factorial(6))
print(factorial(1))
print(factorial(13))
print(factorial(9))

#print("\n")
#countdown(5)


print("\nFIBONACCI: ")
print(fibonacci(5))
print(fibonacci(1.5))
print(fibonacci(-1.5))
print(fibonacci(-4))