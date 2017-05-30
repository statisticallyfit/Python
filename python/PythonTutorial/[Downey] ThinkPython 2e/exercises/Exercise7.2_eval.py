import math


def evalInput():
    expr = input("Input your expression: ")
    while "done" not in expr.lower():
        print(eval(expr))
        expr = input("\nInput your expression: ")
    print("DONE")



evalInput()