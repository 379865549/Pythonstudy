import numpy as np 

# 指定一个数组，并使用 [0, 1) 区间随机数据填充，这些数据均匀分布。
print(np.random.rand(2,5))
print(np.random.randn(1, 10))
# numpy.random.randn(d0, d1, ..., dn) 与 numpy.random.rand(d0, d1, ..., dn) 的区别在于，前者是从标准正态分布中返回一个或多个样本值。
# randint(low, high, size, dtype) 方法将会生成 [low, high) 
# 的随机整数。注意这是一个半开半闭区间。