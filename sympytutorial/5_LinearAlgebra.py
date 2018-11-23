# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.5
# ---

from sympy import *
init_printing()
from sympy.matrices import *
from numpy import *

M = Matrix([[1,0,0], [0,0,0]])
M

Matrix([M, (0,0,-1)])

Matrix(2, 3, [1,2,3,4,5,6]) #2 by 3 matrix with these values

Matrix(4, 7, arange(28).astype(int))

# +
#create eye matrix
def eye(i, j):
    if i == j:
        return 1
    else:
        return 0

Matrix(4, 4, eye)
# -

Matrix(3, 4, lambda i, j: 1 - (i+j) % 2)

eye(4)
#double eye matrix
eye(4)

zeros(2)

# +
#zeros(5, 2) #doesn't work??
# -

ones(3)

# +
#ones(1, 5) #doesn't work??
# -

diag(1, Matrix([1,2], [3,4]))
# double
diag(1, Matrix([1,2], [3,4]))

from sympy import *
init_printing()










