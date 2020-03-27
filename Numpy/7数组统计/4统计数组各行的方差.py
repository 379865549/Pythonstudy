import numpy as np 
a = np.array(([1, 4, 3], [6, 2, 9], [4, 7, 2]))
print(a)
print("各行方差",np.var(a,axis=1))