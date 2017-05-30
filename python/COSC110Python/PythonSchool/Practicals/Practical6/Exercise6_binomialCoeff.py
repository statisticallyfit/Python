
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



# note: the answer

# list comprehension
def binomialCoeffListComp(n, k):
    '''Compute binomial coefficient n choose k: nCk.
        n: number of trials
        k: number of successes

        returns: int
    '''
    return 1 if k == 0 else 0 if n == 0 or k > n \
        else (binomialCoeffListComp(n-1, k) + binomialCoeffListComp(n-1, k-1))
