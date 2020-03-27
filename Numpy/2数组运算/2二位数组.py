import numpy as np 

#二维数组可以看成矩阵
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A,"\n",B)
print("加法\n",A+B)
print("减法\n",A-B)
print("乘法\n",A*B)
print("除法\n",A/B)
print("矩阵乘法\n",np.mat(A) * np.mat(B))#把A和B定义为矩阵
print(np.dot(A, B))#矩阵乘法
print("数乘矩阵\n",2 * A)
print("转置\n",A.T)
print("求逆\n",np.linalg.inv(A))