

# recursion
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


# Recrusion 2
def printN(s, n):
    if n <= 0:
        return
    print(s)
    printN(s, n-1)




def sequence(n, m):
    if n < 0 and m < 0:
        return n * m
    print(n, m)
    if m > n:
        return sequence(m, n)
    return sequence(n-1, m)




def testExam2(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1


print("\nTEST EXAM2: ")
testExam2(24)



print("\nCOUNTDOWN:")
countdown(5)

print("\n")
printN("happy", 10)

print("\nSEQUENCE: ")
print(sequence(1, 0))