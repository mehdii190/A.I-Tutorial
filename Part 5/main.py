import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer


country = pd.read_csv('/Users/mehdimirawa/Desktop/video IA/c_data.csv',header=2)

#print(country)


country =country.rename(columns={' CountryName':'Name','CountryCode':'Code','Total population':'pop'})
country.drop('1',axis=1,inplace=True)
country.drop('Code',axis=1,inplace=True)


country.rename(index=country.Name,inplace=True)
country.drop('Name',axis=1,inplace=True)


#print(country.info())

#print(country.describe())


#print(type(country))
#max_pop = country['pop'].max()
#print(country[country['pop']==max_pop])

#country.drop('World',axis=0,inplace=True)



#country.replace('?',np.nan,inplace=True)
#print(country.isnull())



#country.dropna(axis=0,inplace=True)
#print(country)


#country.fillna(0,inplace=True)
#print(country)


#country.fillna({'pop_growth':0,'pop':10000000,'Area':50000},inplace=True)
#print(country)




#country.fillna(method='ffill',inplace=True)
#print(country)




#importer = SimpleImputer(missing_values=np.nan, strategy='mean')
#importer.fit(country)
#country2=importer.transform(country)
#print(country2)

#print(country.mean())





#my_data = np.array([[1,'a','A'],[2,'a','A'],[2,'a','A'],[3,'a','A'],[4,'a','A'],[4,'a','A']])
#my_data=pd.DataFrame(my_data,index=[0,1,2,3,4,5],columns=['column1','column2','column3'])
#print(my_data)


#print(my_data.duplicated())


#my_data.drop_duplicates(inplace=True)
#print(my_data)





my_source1=pd.DataFrame([[0,10,13,17,17],[0,12,14,14,15],[0,13,17,12,20],[0,14,12,18,19]])
my_source1[0]=['babak','raha','sara','reza']
#print(my_source1)
my_source2=pd.DataFrame([[0,10,13,17],[0,12,15,20],[0,13,17,12],[0,14,12,17],[0,15,15,18],[0,14,12,18]])
my_source2[0]=['babak','baran','sara','arash','mahan','reza']
#print(my_source2)





my_concat=pd.concat([my_source1,my_source2],axis=0,ignore_index=True)
print(my_concat)



my_concat.drop_duplicates(0,inplace=True)
print(my_concat)



my_concat.fillna(0,inplace=True)
my_concat.reset_index(drop=True,inplace=True)
print(my_concat)





