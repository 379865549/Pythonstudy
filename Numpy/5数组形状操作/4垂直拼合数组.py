import numpy as np 
a = np.random.randint(10,size=(3,3))
b = np.random.randint(10,size=(3,3))
print(a,"\n",b)
print(np.vstack((a,b)))