import numpy as np

arr = np.array([[1,2,3],[4,5,6],['a','b','c']])
print(arr)
print(arr[2][2])

lst=[[1,2,3],[4,5,6],['a','b','c']]
arr=np.array(lst)
print(arr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.dtype)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
newrow=['a','b','c']
arr2=np.vstack([arr,newrow])
print(arr2)

ar1=np.array([[1,2],[4,6]])
ar2=np.array([[1,2],[4,6]])
ar3=np.multiply(ar1,ar2)
print(ar3)

ar1=np.array([[1,2],[4,6]])
ar2=np.array([[1,2],[4,6]])
ar3=np.dot(ar1,ar2)
print(ar3)

a=np.array([[1,2],[4,6]])
k=np.prod(a)  #1*2*4*6
print(k)


ar=np.ones((4,4))
print(ar)
ar2=np.zeros((4,4))
print(ar2)


a=np.array([[1,2],[4,6]])
print(a+5)

c=np.array([[1,2,3,1]])
b=np.ones((4,4))
print(b+c)

a=np.array([[1,2],[4,5]])
print(np.sum(a))

arr1=np.array([[1,2],[4,7]])
arr2=np.array([[1,2],[4,7]])
arr3=np.subtract(arr1,arr2)
print(arr3)


arr1=np.array([[1,2],[4,7]])
arr2=np.array([[1,2],[4,7]])
arr3=np.divide(arr1,arr2)
print(arr3)



arr1=np.array([[1,2],[4,7]])
arr3=np.floor_divide(arr1,2)
print(arr3)


print(np.math.sqrt(1334))
#np.math.inf




print(np.random.uniform(1,10))
ar=np.random.uniform(1,10,(3,3))
print(ar)










