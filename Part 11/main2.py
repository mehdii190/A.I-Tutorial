import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns






data = pd.read_csv("/Users/mehdimirawa/Desktop/video IA/banking.csv")

#print(data.head())


temp= data.head()


print(data.info())

print(data["education"].unique())




data["education"]=data["education"].replace(["basic.4y","basic.6y","basic.9y"],"basic")
print(data["education"].unique())


##############

print(data["y"].value_counts())
sns.countplot(x="y",data=data)
plt.show()
###############

count_no_sub = len(data[data["y"]==0])
count_sub = len(data[data["y"]==1])
pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
print("percentage of no sub is", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)
print("percentage of sub ", pct_of_sub*100)
################


#myexplore=data.groupby("y").mean()



#####################



myexplore=data.groupby("job").mean()


#########



pd.crosstab(data.job, data.y).plot(kind="bar")
plt.title("prachashe")
plt.xlabel("job")
plt.ylabel("freq of purchase")
plt.show()


############

table = pd.crosstab(data.marital,data.y)
z = table.div(table.sum(1).astype(float), axis=0)
table.div(table.sum(1).astype(float),axis=0).plot(kind="bar")
plt.title("stacked bar char")
plt.xlabel("marital ")
plt.ylabel("proportion")
plt.show()



############


x=0
xx=(data.columns.values)
for i in range(len(xx)-1):
    table=pd.crosstab(data.iloc[:,x],data.y)
    z=table.div(table.sum(1).astype(float),axis=0)
    table.div(table.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True)
    plt.title("Stacked Bar Chart Of Marital Status vs Purchase")
    plt.xlabel("Marital Status")
    plt.ylabel("Proportion")
    plt.show()
    x=x+1

























