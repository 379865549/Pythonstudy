import numpy as np 

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10]])
c = np.array([[11, 12]])
print(np.concatenate((a, b, c), axis=0))