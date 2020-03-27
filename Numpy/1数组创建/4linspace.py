import numpy as np
# 在区间 [3, 7) 中以 0.5 为步长新建数组
print(np.linspace(3,7,0.5,dtype='float32'))
""" endpoint：布尔值，如果为真，则最后一个样本包含在序列内。 """
print(np.linspace(0,10,10,endpoint=True))
print(np.linspace(0,10,10,endpoint=False))