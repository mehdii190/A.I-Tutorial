import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
import seaborn as sb

sl1 = pd.read_csv("I:/video I.A/exam/salary_data_first.csv")
sl2 = pd.read_csv("I:/video I.A/exam/salary_data_second.csv")


sl1.drop("pre",axis=1,inplace=True)
sl2.drop("pre",axis=1,inplace=True)


##########################################

sl_df = pd.concat([sl1,sl2],axis=0,ignore_index=True)
#################################

sl_df.replace('?',np.nan,inplace=True)
new_df = sl_df.dropna()
new_df.reset_index(drop=True,inplace=True)
new_df.fillna(0,inplace=True)
new_df = new_df.astype(float)
#################################

x = new_df.iloc[:, :-1].values
y = new_df.iloc[:, -1].values


#################################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

reg = LinearRegression()

reg.fit(x_train,y_train)

y_pred =reg.predict(x_test)
################################

print("R2 Reg: ", reg.score(x_test, y_test))

##################################

plt.scatter(x_test, y_test, c="b")
plt.scatter(x_train, y_train, c="r")
plt.plot(x_test,y_pred, c="brown")
plt.title("linear reg")
plt.xlabel("Years experience")
plt.ylabel("Salary")
plt.show()
###############
#new_df.boxplot()
#plt.show()

###############################

mse =mean_squared_error(y_test, y_pred)
print("mse===> ", mse ," <===##" )

################################

df_scores = cross_val_score(reg, x , y, scoring="r2",cv=5)
print("df score: ",df_scores)
print("mean score: ",np.mean(df_scores))


###############################

new_df.boxplot(column=["Salary"])
plt.show()

print(new_df['Salary'].describe())


uppper_boundary=new_df['Salary'].mean() + 3* new_df['Salary'].std()
lower_boundary=new_df['Salary'].mean() - 3* new_df['Salary'].std()
print("lower : ",lower_boundary), print("upper : ",uppper_boundary),print("mean : ",new_df['Salary'].mean())

################################

new_df.boxplot(column=["YearsExperience"])
plt.show()

print(new_df['YearsExperience'].describe())


uppper_boundary=new_df['YearsExperience'].mean() + 3* new_df['YearsExperience'].std()
lower_boundary=new_df['YearsExperience'].mean() - 3* new_df['YearsExperience'].std()
print("lower : ",lower_boundary)
print("upper : ",uppper_boundary)
print("mean : ",new_df['YearsExperience'].mean())























