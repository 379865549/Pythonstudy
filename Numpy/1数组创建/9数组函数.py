import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
# ndarray.T 用于数组的转置，与 .transpose() 相同。
print(a.T)
# ndarray.dtype 用来输出数组包含元素的数据类型。
print(a.dtype)
# ndarray.imag 用来输出数组包含元素的虚部。
print(a.imag)
# ndarray.real用来输出数组包含元素的实部。
print(a.real)
# ndarray.size用来输出数组中的总包含元素数。
print(a.size)
# ndarray.itemsize输出一个数组元素的字节数。
print(a.itemsize)
# ndarray.nbytes用来输出数组的元素总字节数。
print(a.nbytes)
# ndarray.ndim用来输出数组维度。
print(a.ndim)
# ndarray.shape用来输出数组形状。
print(a.shape)
# ndarray.strides用来遍历数组时，输出每个维度中步进的字节数组。
print(a.strides)