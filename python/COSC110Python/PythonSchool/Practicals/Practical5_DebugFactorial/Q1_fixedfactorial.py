def factorial(n):
    """Calculate the factorial of the given value and return the result.
        The factorial of n is the product of all positive integers less than or equal to n.
        Keyword arguments:
        n -- A positive integer
    """
    if n < 0: return 0

    result = 1
    while n > 1: # FIXED: should be > 1 not != 0 to avoid having n < 0 and avoid returning 1! = 0 because 1! = 1
        # FIXED: must switch these statements to avoid having factorial less than one given (calculate n! not (n-1)!
        result = result * n
        n -= 1

    return result

# Calculate factorial for the first four integers
for num in range(-1, 10):
    print('Factorial of', num, 'is', factorial(num))


# Unit testing
assert factorial(-3) == 0
assert factorial(-2) == 0
assert factorial(-1) == 0
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120