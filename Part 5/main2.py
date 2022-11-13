import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import scale , normalize, minmax_scale
from sklearn.impute import SimpleImputer
import seaborn as cb

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


#scale_data = scale(smartphones_data)
#df_data = pd.DataFrame(scale_data,index=smartphones_data.index,columns=smartphones_data.columns)







#scale_data = scale(smartphones_data, norm='l2',axis=0)
#df_data = pd.DataFrame(scale_data,index=smartphones_data.index,columns=smartphones_data.columns)


#df=[[1,3,4],[2,3,1]]
#scale_data=normalize(df,norm="l2", axis=0)



#scale_data = minmax_scale(smartphones_data, feature_range=(0,1))
#df_data = pd.DataFrame(scale_data,index=smartphones_data.index,columns=smartphones_data.columns)




#y = [6,6,7,5,7,3,7,10,22,8]
#cb.boxplot(y=y,data=smartphones)
#plt.show()



ar = np.array([1,2,3,4,10,27])
df=pd.DataFrame(ar)

print(df.quantile(0.5))


print(df.quantile(0.25))


print(df.quantile(0.75))

