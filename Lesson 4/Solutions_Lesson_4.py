import numpy as np

# --------------------------------------------------------------------------------------------------------------

# Exercise 1:

# Write a function that takes as input 2 vectors represented as numpy arrays
# and prints the dot product between the 2 vectors

# Hint: https://numpy.org/doc/stable/reference/generated/numpy.dot.html

# --------------------------------------------------------------------------------------------------------------

# Exercise 2:

# Create two random 2 x 2 matrices using 2-dimensional numpy arrays, name them A and B and print the
# matrix C where C is the resulting matrix of multiplying A transpose with B

# Hint: https://numpy.org/doc/stable/reference/generated/numpy.transpose.html

# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------

# Exercise 3:

# Write a function that takes a row vector v1 of length 3, a 3 x 3 matrix M and a column vector v2 of length 3
# and returns the value v that results by multiplying the row vector from the left on the matrix and the column
# vector from the right on the matrix, schematically shown as v = v1 M v2

# --------------------------------------------------------------------------------------------------------------























# Solutions

# 1

def dot(v1, v2):

    return np.dot(v1, v2)

# 2

A = np.random.rand(2, 2)
B = np.random.rand(2, 2)
print(np.matmul(np.transpose(A), B))

# 3

def exercise_3(v1, M, v2):

    # Let v_temp = v1 M such that v = v1 M v2 = v_temp v2

    v_temp = np.matmul(v1, M) # does v1 M
    v = np.matmul(v_temp, v2) # does v_temp v2

    # v is a 1 x 1 matix so to make it into a number we index it

    result = v[0][0]

    return result

v1 = np.random.rand(1, 3) # row vector

M = np.random.rand(3, 3) # matrix

v2 = np.random.rand(3, 1) # column vector

v = exercise_3(v1, M, v2)

print(v)