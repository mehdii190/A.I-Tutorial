import pandas as pd
import numpy as np
from sklearn import preprocessing


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

country.drop('World',axis=0,inplace=True)

