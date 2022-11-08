import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import scale , normalize, minmax_scale
from sklearn.impute import SimpleImputer


smartphones = pd.read_csv('/Users/mehdimirawa/Desktop/video IA/smartphones.csv')

#print(smartphones.describe())
#print(smartphones.OS.value_counts())



#cat_os = smartphones.groupby(smartphones['OS'])

#print(cat_os.mean())


#x = pd.crosstab(smartphones.OS,smartphones.Capacity)
#print(x)


#x = pd.pivot_table(smartphones,index = 'Name',columns ='Company',values = 'Ram')
#print(x)

#############################################

#smartphones.rename(index = smartphones.Name,inplace=True)
#smartphones.drop(['Name','Company'],axis=1,inplace=True)



smartphones_data = pd.get_dummies(smartphones)




#################################################

#df = [2,4,4,4,5,5,7,9]
#scale_data = scale(df)


scale_data = scale(smartphones_data)
df_data = pd.DataFrame(scale_data,index=smartphones_data.index,columns=smartphones_data.columns)






