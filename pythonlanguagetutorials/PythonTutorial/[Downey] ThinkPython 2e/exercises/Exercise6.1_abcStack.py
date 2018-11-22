

def b(z):
    prod = a(z,z)
    print(z, prod)
    return prod


def a(x,y):
    x += 1
    return x*y

def c(x, y, z):
    square = b(x + y + z) ** 2
    return square


# main program
x = 1
y = x + 1
print(c(x, y+3, x+y))