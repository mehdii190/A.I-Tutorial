import numpy as np

a = np.arange(2,34,2).reshape([4,4])
print(a)

#####################################
#b = np.array([[1,2,3],[4,5,6],[7,8,9]])
#c = b[1:2,1:2]
#print(c)
#######################################

arr=np.ones((10,10))
place1 = arr[1:9,1:9]=0
print(arr)