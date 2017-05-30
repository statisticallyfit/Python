import math



# a is power of b if a is divisible by b and a/b is power of b
def isPower(a, b):
    if(a == b):
        return True
    elif a % b != 0:
        return False
    return isPower(a // b, b)


# question solving: is there n such that 2^n = 16?
assert isPower(16, 2), "test 1"; print(math.log(16, 2))
assert isPower(512, 2), "test 2"; print(math.log(512, 2))
assert not isPower(36, 2), "test 3"; print(math.log(36, 2))
assert isPower(27, 3), "test 4"; print(math.log(27, 3))
assert not isPower(6, 4), "test 5"; print(math.log(6, 4))
assert isPower(64, 8), "test 6"; print(math.log(64, 8))
assert not isPower(8, 64), "test 7"; print(math.log(8, 64))