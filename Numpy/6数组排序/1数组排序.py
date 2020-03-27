import numpy as np 
a = np.array(([1,4,3],[6,2,9],[4,7,2]))
print(a)
print("最大值",np.max(a,axis=0))#返回每列的最大值
print("最小值",np.min(a,axis=1))#返回每列最小值
print("每列最大值索引",np.argmax(a,axis=0))#返回每列最大索引
print("每行最小值索引",np.argmin(a,axis=1))#返回每行最小索引