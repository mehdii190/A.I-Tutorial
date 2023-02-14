import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

#-----------------------csv---------------------------
#The classification goal is to predict whether the client will subscribe (1/0) to
# a term deposit (variable y). 
data=pd.read_csv("/Users/mehdimirawa/Desktop/video IA/banking.csv")
#print(data.head)
#print(data.shape)
#print(data.info())
#print(data.describe)
#temp=data.loc[:4,:]

#---------------------------- preprocessing -----------------------------------

#education feature has a lot of category
#and we need to reduce the categories for a better modelling. 
#print(data['education'].unique())
#Let us group “basic.4y”, “basic.9y” and “basic.6y” together and call them “basic”.

data['education']=data['education'].replace(["basic.4y","basic.6y","basic.9y"],"basic")
# print(data['education'].unique())


#*******************#
###let process the values

#print(data['y'].value_counts())
#sns.countplot(x='y',data=data) #y is our label column name in dataset
#plt.show()

###below calculation show that our data is imbalance (88% to 11%)

#count_no_sub = len(data[data['y']==0])
#count_sub = len(data[data['y']==1])
#pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
#print("percentage of no subscription is", pct_of_no_sub*100)
#pct_of_sub = count_sub/(count_no_sub+count_sub)
#print("percentage of subscription", pct_of_sub*100)

### more exploration
#myexplore=data.groupby('y').mean()
'''
above code show that:
    The average age of customers who bought the term deposit is higher than that of the customers who didn’t.
    The pdays (days since the customer was last contacted) is understandably lower for the customers who bought it. The lower the pdays, the better the memory of the last call and hence the better chances of a sale.
'''
### we can calculate another features
#myexplore=data.groupby('job').mean()

#------------------------------------Visualization ---------------------------------
### fig 1 ###
'''The frequency of purchase of the deposit depends a great deal on the job title.
Thus, the job title can be a good predictor of the outcome variable.'''
#pd.crosstab(data.job,data.y).plot(kind='bar')
#plt.title('Purchase Frequency for Job Title')
#plt.xlabel('Job')
#plt.ylabel('Frequency of Purchase')
#plt.show()

### fig 2 ###
#table=pd.crosstab(data.marital,data.y)
#z=table.div(table.sum(1).astype(float), axis=0) #all of table values are devided to sum of rows and sum(1) is axis x
#table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
#plt.title('Stacked Bar Chart of Marital Status vs Purchase')
#plt.xlabel('Marital Status')
#plt.ylabel('Proportion of Customers')
#plt.show()
'''above fig show that The marital status does not seem a strong predictor for the outcome variable.'''

### fig 3 ###
#table=pd.crosstab(data.education,data.y)
#table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
#plt.title('Stacked Bar Chart of Education vs Purchase')
#plt.xlabel('Education')
#plt.ylabel('Proportion of Customers')
#plt.show()

'''above fig show that The education status seem a strong predictor for the outcome variable.'''

#pd.crosstab(data.day_of_week,data.y).plot(kind='bar')
#plt.title('Purchase Frequency for Day of Week')
#plt.xlabel('Day of Week')
#plt.ylabel('Frequency of Purchase')
#plt.show()

'''above bad'''

#pd.crosstab(data.month,data.y).plot(kind='bar')
#plt.title('Purchase Frequency for Month')
#plt.xlabel('Month')
#plt.ylabel('Frequency of Purchase')
#plt.savefig('pur_fre_month_bar')

'''above good '''

#data.age.hist()
#plt.title('Histogram of Age')
#plt.xlabel('Age')
#plt.ylabel('Frequency')
#plt.savefig('hist_age')

''' above: Most of the customers of the bank in this dataset are in the age range of 30–40.'''

#pd.crosstab(data.poutcome,data.y).plot(kind='bar')
#plt.title('Purchase Frequency for Poutcome')
#plt.xlabel('Poutcome')
#plt.ylabel('Frequency of Purchase')
#plt.show()

''' above: Poutcome seems to be a good predictor of the outcome variable.'''

# turn categorical features to dummy features
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1

### below eliminate the categorical features from dataset
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=data[to_keep]
temp=data_final.columns.values

###################################### imbalanced data #############################################
'''Classification models attempt to categorise data into different buckets. 
In an imbalanced dataset, one bucket makes up a large portion of the training dataset (the majority class)
 while the other bucket is underrepresented in the dataset (the minority class).'''

###sample:
'''Consider the case of collecting training data for a model predicting medical conditions.
 Most of the patient data collected, let’s say 95 percent, will likely fall into the healthy bucket
 while the sick patients make up a much smaller portion of the data.
 During training, the classification model learns that it can achieve 95 percent accuracy
 if it predicts “healthy” for every piece of data it encounters.
 That’s a huge problem because what doctors really want the model to do is identify
 those patients suffering from a medical condition.''' 
 
 #### SMOT: Synthetic Minority Oversampling Technique
'''One way to solve this problem is to oversample the examples in the minority class.
This can be achieved by simply duplicating examples from the minority class in the training dataset prior to fitting a model. 
This can balance the class distribution but does not provide any additional information to the model.'''
 
X = data_final.loc[:, data_final.columns != 'y']
y = data_final.loc[:, data_final.columns == 'y']
from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)

######
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns
os_data_X,os_data_y=os.fit_resample(X_train, y_train)
######

os_data_X,os_data_y=os.fit_resample(X, y)
columns = X.columns
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])

#####
'''Now we have a perfect balanced data! You may have noticed that I over-sampled only on the training data,
because by oversampling only on the training data, 
none of the information in the test data is being used to create synthetic observations,
therefore, no information will bleed from test data into the model training.'''

#####
# we can Check the numbers of our data
#print("length of oversampled data is ",len(os_data_X))
#print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['y']==0]))
#print("Number of subscription",len(os_data_y[os_data_y['y']==1]))
#print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_X))
#print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_X)) 
 
#####################################################  
 
#data_final_vars=data_final.columns.values.tolist()
#y=['y']
#X=[i for i in data_final_vars if i not in y]
#from sklearn.feature_selection import RFE
#logreg = LogisticRegression(solver='lbfgs',max_iter=2000)
#rfe = RFE(logreg,  n_features_to_select=20)
#rfe = rfe.fit(os_data_X, os_data_y.values.ravel()) #ravel will flatten the data
#print(rfe.support_)
#print(rfe.ranking_)

cols=['euribor3m', 'job_blue-collar', 'job_housemaid', 'marital_unknown', 'education_illiterate', 'default_no', 'default_unknown', 
      'contact_cellular', 'contact_telephone', 'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 
      'month_may', 'month_nov', 'month_oct', "poutcome_failure", "poutcome_success"] 
X=os_data_X[cols]
y=os_data_y['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print(logreg.score(X_test, y_test))
#print(y_pred)



#############

from sklearn.metrics import confusion_matrix

conf = confusion_matrix(y_test, y_pred)

print(conf)

































