import numpy as np
import pandas as pd

c=np.random.randint(5,10)
a=np.random.randint(1,100 ,size=c)
b=pd.Series(a)
print(b)


########################################

a = np.random.randint(5,10)
b= np.random.randint(1,100 ,size= a)
c= np.array(b)
f = pd.Series(c)
print(f)