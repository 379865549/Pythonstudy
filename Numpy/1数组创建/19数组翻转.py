import numpy as np 
#    fliplr(m)：左右翻转数组。
#    flipud(m)：上下翻转数组。


a = np.arange(16).reshape(4, 4)
print(np.fliplr(a))
print(np.flipud(a))