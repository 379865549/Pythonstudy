import numpy as np 

a = np.ones((1, 2, 3))
print(np.moveaxis(a, 0, -1))
print(a.shape)
print(np.moveaxis(a, 0, -1).shape)

a = np.arange(4).reshape(2, 2)
print(np.asmatrix(a))  # 将二维数组转化为矩阵类型