import numpy as np

arrObj = np.array([4,5,7,90])
floatArr = arrObj.astype('f')
print(floatArr)

arrObj = np.array([1.3, 6.8, 3.5, 9.2])
intArr = arrObj.astype('i')
print(intArr)


arrObj = np.array([[12, 43, 21], [67, 32, 98]])
print(arrObj.shape)


arrObj = np.array(["Python", "JavaScript", "Solidity", "Golang"])
print(np.sort(arrObj))
##################################################################

a = np.array([1, 2, 3])
print(a)

a1=np.arange(4)
print(a1)

a2=np.arange(2, 9, 2)
print(a2)

a3=np.linspace(0, 10, num=5)
print(a3)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((b, a)))


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))



array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example.ndim)
print(array_example.size)
print(array_example.shape)

a = np.arange(6)
b = a.reshape(3, 2)
print(b)
print(np.reshape(a, newshape=(1, 6), order='C'))

a = np.array([1, 2, 3, 4, 5, 6])
col_vector = a[:, np.newaxis]
print(col_vector.shape)

arr=np.diag([1, 2, 3])
print(arr)



