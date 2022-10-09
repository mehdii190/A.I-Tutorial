import numpy as np
import pandas as pd

a = np.array([1,0,3,10,100])
labeled_a = pd.Series(a)
print(labeled_a)
print(type(labeled_a))

dct={'a':125,'b':845,'c':555}
ser=pd.Series(dct)
print(ser)
