import numpy as np 


a = np.arange(10)
print(a.resize(2, 5))
print(a)
# 你可能会纳闷了，这个 resize 看起来和上面的 reshape 一样呢，都是改变数组原有的形状。

""" 其实，它们是有区别的，区别在于对原数组的影响。reshape 在改变形状时，不会影响原数组，相当于对原数组做了一份拷贝。而 resize 则是对原数组执行操作。
翻转数组 """