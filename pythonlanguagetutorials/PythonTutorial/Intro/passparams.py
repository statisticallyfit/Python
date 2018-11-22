

x = [1,2,3]
n = 10

def f(a, b):
    print(a is x)
    a[0] = 7
    b = 11
    print("b is %d" % b)
    
print("before call n is %d" % n)
print(x[0])

f(x, n)     # copy of n is made through b
print("after call n is %d" % n)
print(x[0])

