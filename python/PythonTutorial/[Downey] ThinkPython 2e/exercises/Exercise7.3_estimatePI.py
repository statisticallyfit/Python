import math

def estimatePI():
    epsilon = 10**(-15)
    oneOverPI = 1103
    k = 1

    currentTerm = math.factorial(4*k)*(1103 + 26390*k)/(math.factorial(k)**4 * 396**(4*k))

    while currentTerm >= epsilon:
        oneOverPI += currentTerm
        k += 1
        currentTerm = math.factorial(4*k)*(1103 + 26390*k)/(math.factorial(k)**4 * 396**(4*k))

    oneOverPI *= 2 * math.sqrt(2)/9801
    return 1 / oneOverPI



print("real:     ", math.pi)
print("estimate: ", estimatePI())