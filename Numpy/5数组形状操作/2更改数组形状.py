import numpy as np 
a = np.random.random((3,2))
print(a)
print(a.reshape(2,3))#不改变原始数组
print(a.resize(2, 3))#改变原始数组