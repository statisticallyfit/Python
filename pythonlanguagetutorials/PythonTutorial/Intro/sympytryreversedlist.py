from sympy import Integer

def list_to_frac(list):
    expr = Integer(0)
    for i in reversed(list[1:]):  #list[x:] means start from index = x
        expr += i
        expr = 1/expr

    return list[0] + expr

list = [5, 2, 3, 4]
print(list_to_frac(list))