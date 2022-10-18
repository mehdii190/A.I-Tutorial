import numpy as np
import pandas as pd


my_array=np.random.uniform(1,10,(4,4))
df=pd.DataFrame(my_array)
my_df=pd.DataFrame(my_array,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
#print(my_df)
#my_df['col1']=my_df['col1'].apply(lambda x:x+1)
#print(my_df)

#my_df.loc[:,'col1':'col2']=my_df.loc[:,'col1':'col2'].apply(lambda x:x+1)
#print(my_df)
#my_df.loc[:,'row2':'row3']=my_df.loc[:,'row2':'row3'].apply(lambda x:x+1)
#print(my_df)

#my_df=my_df.apply(lambda x:x+1)
#print(my_df)

#my_df.sort_index(axis=1,ascending=False,inplace=True)
#print(my_df)

#my_df.sort_values(by='col1',ascending=False,inplace=True)
#print(my_df)


#print(my_df.tail(2))

data=pd.read_csv('earthquakes.csv')
print(data)