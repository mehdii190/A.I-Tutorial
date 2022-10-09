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
############################################## part 2
ar=np.arange(1,10,2,dtype='float')
print(ar)


ar2=np.linspace(1,10,15)
print(ar2)


a=np.array([[1,2,3],[4,5,6]])
my_mask2=np.logical_and(a>1,a<=4)
print(a[my_mask2])


a=np.array([1,2,3,4,1,2])
print(np.unique(a))

a=np.array([[1,2,3],[4,5,6]])
print(a)


arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=arr1[:2,:]
print(arr2)


arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=arr1[:,1:2]
print(arr2)



arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=arr1[-1:,-1:]
print(arr2)


arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=arr1[2:,2:]
print(arr2)

arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=np.flip(arr1[:1,:])
print(arr2)


arr1=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr2=np.flip(arr1[:1,::-1])
print(arr2)


arr1=np.array([[1,2,8],[4,5,6],['a','b','c']])
arr2=np.array([[1,2,3],[4,5,6],['a','b','c']])
arr3=np.union1d(arr1,arr2)
arr=np.intersect1d(arr1,arr2)
print(arr)
print(arr3)


a=np.array([1,2,10,100])
print(np.mean(a))


a=np.array([1,2,10,98,100])
print(np.median(a))


a=np.array([1,2,3])
print(np.polyval(a,12))


a=np.array([1,2,3])
print(np.polyder(a))


a=np.array([1,2,3])
print(np.polyint(a))


x = np.array([5,1,2,3])
print(np.all(x))


x = np.ones((5,5)) * -4
print(x)



ar=np.zeros(16).reshape(4,4)
print(ar)


a= np.arange(10,26).reshape(4,4)
print(a)


x =np.diag([1,2,3,4,5])
print(x)


x = np.array([[0,1],[2,3]])
print(x)
print(np.sum(x))
print(np.sum(x , axis=0))
print(np.sum(x, axis=1))


nums = np.array([[3,2,np.nan,1],
                 [10,12,10,9],
                 [5,np.nan,1,np.nan]])
print(nums)
print(np.isnan(nums))


nums = np.array([[5.54,3.38,7.99],
                 [3.34,4.38,6.99],
                 [1.54,2.39,9.29]])
print(nums)
print(np.sort(nums))
print(np.sort(nums,axis=0))



nums = np.array([[5.54,3.38,7.99],
                 [3.34,4.38,6.99],
                 [1.54,2.39,9.29]])
print(nums)
n = 5
print('\nElements of the said array greater then',n , "<")
print(nums[nums>n])
n = 6
print('\nElements of the said array less then',n, ">")
print(nums[nums<n])


nums = np.array([[5.54,3.38,7.99],
                 [3.34,8.32,6.99],
                 [1.54,2.39,9.29]])
print("orginal array ")
print(nums)
n = 8.32
r = 18.32
print(np.where(nums == n, r, nums))

