


# keep dividing b by the remainder of a/b until remainder is zero. When
# that happens, the pair number is the gcd.
def gcd(a, b):
    if b == 0:
        return a
    elif b > a:
        return gcd(b, a)
    else:
        return gcd(b, a % b)



print(gcd(36, 15))
print(gcd(36, 12))
print(gcd(481, 78))