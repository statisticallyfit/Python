# from sympy import *
# from numpy import *
import numpy as np
import sympy as sp

def norm(u):
    sum = 0
    for i in range(len(u)):
        sum += sp.Rational(sp.sympify(u[i]**2))
    return sp.sqrt(sp.sympify(sum))

def unitVector(u):
    results = []
    normValue = norm(u)
    for i in range(len(u)):
        #results.append(sp.Rational(sp.sympify(u[i]), normValue))
        results.append(u[i]/normValue)
    return results

def main():
    w = np.array([sp.Rational(1, 2), sp.Rational(-1, 3), sp.Rational(3, 4)])
    print(unitVector(w))

if __name__ == '__main__':
    main()