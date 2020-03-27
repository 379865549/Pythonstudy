import numpy as np 
# 重设形状
print(np.arange(10).reshape((5, 2)))
# 数组展开 ravel 的目的是将任意形状的数组扁平化，变为 1 维数组。
a = np.arange(10).reshape((5, 2))
print(np.ravel(a))
# order 表示变换时的读取顺序，默认是按照行依次读取，
# 当 order='F' 时，可以按列依次读取排序。
print(np.ravel(a, order='F'))