# Execute the below instructions in Jupiter QtConsole
# line by line.

import numpy as np

# Vector
v = np.array([1, 3, 5, 7])


# Matrix
A = np.mat([[1, 2], [3, 3]])
# Out:  matrix([[1, 2], [3, 3]])


# Adding, subtracting, multiplying matrixes
A + A
# Out: matrix([[2, 4], [6, 6]])

A - A
# Out: matrix([[0, 0], [0, 0]])

A * A
# Out:  matrix([[ 7, 8], [12, 15]])


# Determinant of a matrix
np.linalg.det(A)
# Out: -3.0000000000000004
# Notice the margin of error is due to floating point arithmetics


# Transposing a matrix
np.matrix.transpose(A)
# Out[12]: matrix([[1, 3], [2, 3]])
