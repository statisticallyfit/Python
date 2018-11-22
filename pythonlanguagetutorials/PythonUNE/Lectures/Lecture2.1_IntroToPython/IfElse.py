
xInput = input("Input x: ")
x = int(xInput)

if x > 10:
    print("x is greater than 10")
elif x == 1:
    print("x is equal to 1")
else:
    print("x is = ", x)



"""
if 0 < x:
    if x < 100:
        print("0 < x < 100")
"""
# if 0 < x and x < 100:
if 0 < x < 100:
    print("x is between 0 and 100 strict")
else:
    print("x is outside the range (0,100)")