
"""
# import partial tool
from functools import partial


def multiply(x,y):
    return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

"""

"""__________________________________________"""
# import
from functools import partial

# function
def operation(u,v,w,x):
    return u*4 + v*3 + w*2 + x

#call
p = partial(operation,5,6,7)  # 8 will go into operation function, u = 5, v=6,w=7,x=8
print(p(8))
