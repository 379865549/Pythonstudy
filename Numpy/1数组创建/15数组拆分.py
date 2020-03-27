import numpy as np 

a = np.arange(10)
print(np.split(a, 5))
a = np.arange(10).reshape(2, 5)
print(np.split(a, 2))