import numpy as np
import pandas as pd


my_array=np.random.uniform(1,10,(4,4))
df=pd.DataFrame(my_array)
print(df)



my_df=pd.DataFrame(my_array,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
print(my_df)



dct={'a':[1,2,3,8],'b':[6,45,12,5],'c':[4,4,0,23],'d':[12,1,0,7]}
df=pd.DataFrame(dct)
print(df)



dct={'a':[1,2,3,8],'b':[6,45,12,5],'c':[4,4,0,23],'d':[12,1,0,7]}
df=pd.DataFrame(dct,index=['row1','row2','row3','row4'])
print(df)


my_array=np.random.uniform(1,10,(4,4))
df=pd.DataFrame(my_array)
my_df=pd.DataFrame(my_array,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])
df2=my_df.loc['row1',:]
print(df2)
print(my_df.values)
df3=my_df.values[0]
print(df3)
df4=my_df.values[0][:]
print(df4)




print("###############")
df2=my_df.values
print(df2[:,1:3])



print('################')
df2=my_df.loc['row1':'row4','col2':'col3']
print(df2)


print("############")
print(my_df.loc['row1']['col2'])
print(my_df['col3'])



print("##############")
print(my_df)
print(my_df.iloc[:,1:3])


print("#########")
my_df['col5']=[7,8,5,3]
print(my_df)




print("################")
newlist=np.random.uniform(1,100,(4,1))
my_df['col6']=newlist
print(my_df)



print('#############')
my_df['col5'],my_df['col6']=[7,6,2,3],[2,7,9,4]
print(my_df)



#print('##############')
#my_df.loc['row5']=[9,9,9,9]
#print(my_df)



print('#############')
my_df.loc['row1':'row2','col1']=0
print(my_df)


####### or ########


my_df.loc[0:2,0]=0
print(my_df)


print("###############")
my_df=my_df.reset_index(drop=True)
print(my_df)
####### or #######

my_df.reset_index(drop=True,inplace=True)
print(my_df)
