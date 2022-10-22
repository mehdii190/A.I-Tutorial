import numpy as np
import pandas as pd



############### soal 2 ################

my_array=np.random.uniform(1,10,(4,4))
df=pd.DataFrame(my_array)
my_df=pd.DataFrame(my_array,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
print(my_df)
col1 = my_df.loc[:,'col1']
print(col1)
