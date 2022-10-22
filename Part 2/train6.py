import numpy as np
import pandas as pd


############ soal 1 pandas #####################

a = np.random.uniform(1,10,(4,4))
b = np.random.uniform(1,10,(4,4))
divide = np.divide(a,b)
multiply = np.multiply(a,b)
sum = np.add(a,b)
subtract = np.subtract(a,b)



print('array 1')
print(pd.DataFrame(a))
print('array 2')
print(pd.DataFrame(b))

print(' run ')
print(pd.DataFrame(divide))
print(pd.DataFrame(multiply))
print(pd.DataFrame(sum))
print(pd.DataFrame(subtract))