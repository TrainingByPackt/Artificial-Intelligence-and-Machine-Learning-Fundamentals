import numpy as np 

A = np.mat([[1,2,3],[4,5,6],[7,8,9]])

print( 'A * A: ', A * A )

print( 'det(A): ', np.linalg.det( A ) )

print( 'transpose(A): ', np.matrix.transpose(A) )