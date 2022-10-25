import numpy as np


array = np.random.randint(1,10,(4,4))
ar = np.array(array)
print(array)
print("###################")
arr = ar[:2, 2:], ar[1:2, :2]
neg = np.negative(arr)
print(neg)

### or

ar[(ar>=3)&(ar<=8)]*=-1
print(ar)