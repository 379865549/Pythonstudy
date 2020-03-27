import numpy as np  # 导入 NumPy 模块

a = np.array([1.1, 2.2, 3.3], dtype=np.float64)  # 指定 1 维数组的数值类型为 float64
print(a, a.dtype)  # 查看 a 及 dtype 类型

print(a.astype(int).dtype)  # 将 a 的数值类型从 float64 转换为 int，并查看 dtype 类型