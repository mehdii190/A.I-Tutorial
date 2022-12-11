from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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




plt.scatter(y_test,y_pred)
plt.plot()
plt.xlabel("prices")
plt.ylabel("predicted prices")
plt.show()






















