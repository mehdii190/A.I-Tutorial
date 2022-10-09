import numpy as np
import pandas as pd


a = np.array([1,0,3,10,100])
labeled_a = pd.Series(a)
print(labeled_a)
print(type(labeled_a))


dct={'a':125,'b':845,'c':555}
ser=pd.Series(dct)
print(ser)


my_series=pd.Series([1,2,99,4,5],index=['row1','row2','row3','row4','row5'])
print(my_series)
print(my_series.values)
print(my_series.index)
print(my_series.row1)
print(my_series['row1'])
my_series.index=['a','b','c','d','f']
print(my_series)



