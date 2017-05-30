
def binomialCoeff(n, k):
    '''Compute binomial coefficient n choose k: nCk.
        n: number of trials
        k: number of successes

        returns: int
    '''
    if k == 0:
        return 1
    if n == 0 or k > n:
        return 0

    result = binomialCoeff(n-1, k) + binomialCoeff(n-1, k-1)
    return result




# memoization:
known = {(0, 0):0, (1, 1):1} # note: dict with (n,k): val, elements
def binomialCoeffMemoiz(n, k):
    if k == 0:
        return 1
    if n == 0 or k > n:
        return 0

    if (n, k) in known.keys():
        return known.get((n, k))
    # else
    result = binomialCoeffMemoiz(n-1, k) + binomialCoeff(n-1, k-1)
    known[(n,k)] = result
    return result



# list comprehension
def binomialCoeffListComp(n, k):
    return 1 if k == 0 else 0 if n == 0 or k > n \
        else (binomialCoeffListComp(n-1, k) + binomialCoeffListComp(n-1, k-1))





import math

# nested conditional expr
def binomialCoeffNested(n, k):
    if k == 0:
        return 1
    if n == 0 or k > n:
        return 0

    nFact = math.factorial(n)
    kFact = math.factorial(k)
    n_kFact = math.factorial(n-k)
    return nFact // (kFact * n_kFact)






assert binomialCoeffNested(0, 1) == 0
assert binomialCoeffNested(5, 4) == 5
assert binomialCoeffNested(5, 1) == 5
assert binomialCoeffNested(5, 2) == 10
assert binomialCoeffNested(9, 4) == 126
assert binomialCoeffNested(4, 9) == 0
assert binomialCoeffNested(1, 1) == 1

assert binomialCoeffListComp(0, 1) == 0
assert binomialCoeffListComp(5, 4) == 5
assert binomialCoeffListComp(5, 1) == 5
assert binomialCoeffListComp(5, 2) == 10
assert binomialCoeffListComp(9, 4) == 126
assert binomialCoeffListComp(4, 9) == 0
assert binomialCoeffListComp(1, 1) == 1

assert binomialCoeffMemoiz(0, 1) == 0
assert binomialCoeffMemoiz(5, 4) == 5
assert binomialCoeffMemoiz(5, 1) == 5
assert binomialCoeffMemoiz(5, 2) == 10
assert binomialCoeffMemoiz(9, 4) == 126
assert binomialCoeffMemoiz(4, 9) == 0
assert binomialCoeffMemoiz(1, 1) == 1

assert binomialCoeff(0, 1) == 0
assert binomialCoeff(5, 4) == 5
assert binomialCoeff(5, 1) == 5
assert binomialCoeff(5, 2) == 10
assert binomialCoeff(9, 4) == 126
assert binomialCoeff(4, 9) == 0
assert binomialCoeff(1, 1) == 1