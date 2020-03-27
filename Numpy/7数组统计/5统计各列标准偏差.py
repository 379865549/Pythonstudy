import numpy as np 
a = np.array(([1, 4, 3], [6, 2, 9], [4, 7, 2]))
print(a)
print("各列的标准偏差",np.std(a,axis=0))