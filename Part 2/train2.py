import numpy as np


################# soal 2 ######################
my_array=np.random.uniform(1,10,(4,4))
print(my_array)
print("####################################")
my_array[:, [0, 1]] = my_array[:, [1, 0]]
my_array[:,[2,3]]=my_array[:,[3,2]]
print(my_array)


