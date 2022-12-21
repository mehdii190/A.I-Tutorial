from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)

boston_df["Price"] = boston.target



x = boston.data
y = boston.target

x_train , x_test , y_train , y_test = train_test_split(x, y ,test_size=0.3,random_state=42)

############### fit 

reg = LinearRegression()
reg.fit(x_train,y_train)

y_pred = reg.predict(x_test)


print(reg.score(x, y))
#print(reg.score(x_train, y_train))


############

plt.scatter(y_test,y_pred)
plt.plot()
plt.xlabel("prices")
plt.ylabel("predicted prices")
plt.show()

############ 


mse =mean_squared_error(y_test, y_pred)
print("**** MSE: ",mse,"****")


#############


#new_x = boston.data[:,[1,2]]
#new_y = boston.target

#new_x_train, new_y_train, new_x_test, new_y_test =train_test_split(new_x,new_y,test_size=0.3,random_state=42)
#new_reg = LinearRegression()
#new_reg.fit(new_x_train,new_y_train)
#new_x_predict = new_reg.predict(new_x_test)


############################################


reg = LinearRegression()
cv_scores = cross_val_score(reg, x , y, scoring="r2",cv=5)
#cv_scores2 = cross_val_score(reg, x,y, scoring="neg_mean_squared_error",cv=5)
print(cv_scores)
print(np.mean(cv_scores))













