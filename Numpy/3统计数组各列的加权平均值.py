import numpy as np 
a = np.array(([1, 4, 3], [6, 2, 9], [4, 7, 2]))
print(a)
print("各列的加权平均值",np.average(a,axis=0))