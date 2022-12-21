import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import scale
#####
imb= pd.read_csv("C:/Users/persian computer/Desktop/website/I.A-Tutorial/my work/csv/IMDB Top 250 Movies.csv")
#####
df = pd.DataFrame(imb)
#####
print(df.head())
print(df.info())
#####

de = df.describe()

df.drop("Movie_Name",axis=1,inplace=True)
print(df.head())

########################

sb.distplot(df[df.columns[0]],kde_kws={"color":"blue","lw":3,"label":"KDE"},hist_kws={"color":"r"})
plt.tight_layout()

########################


x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


########################


#########
#new_df = pd.get_dummies(df)
#scd = scale(new_df)

#ok = pd.DataFrame(new_df.data,columns=new_df.feature_names)

#ok[new_df.index] = x.
################

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3,random_state=42)

reg =LinearRegression()
reg.fit(x_train,y_train)

y_pred = reg.predict(x_test)

print(reg.score(x, y))


plt.scatter(x_test, y_test, c="b")
plt.scatter(x_train, y_train, c="r")
plt.plot(x_test,y_pred, c="brown")
plt.title("imb")
plt.xlabel("Years")
plt.ylabel("rate")
plt.show()




mse = mean_squared_error(y_test, y_pred)
print(mse)





