import numpy as np 
a = np.arange(12).reshape(3, 4)
print(a)
print(np.delete(a, 2, 1))
# 这里代表沿着横轴，将第 3 列(索引 2)删除。
# 当然，你也可以沿着纵轴，将第三行删除。
print(np.delete(a, 2, 0))