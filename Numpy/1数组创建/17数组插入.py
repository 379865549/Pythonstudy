import numpy as np 

a = np.arange(12).reshape(3, 4)
b = np.arange(4)
# insert(arr，obj，values，axis)：依据索引在特定轴之前插入值。
print(np.insert(a, 2, b, 0))
a = np.arange(6).reshape(2, 3)
b = np.arange(3)

print(np.append(a, b))
# 注意 append方法返回值，默认是展平状态下的 1 维数组。
