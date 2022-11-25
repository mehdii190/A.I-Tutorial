from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()


##########################

#print(iris.data.shape)
#print(iris.feature_names)

##########################



iris_df = pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df['target']=iris.target


###########################

#pd.plotting.scatter_matrix(iris_df,c=iris.target)


###########################


#x = iris.data
#y = iris.target

###########################

knn = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)
x = iris.data
y = iris.target
#knn.fit(x,y)

###########################

#x_new = np.array([[ 5.8, 4, 1.2, 0.2]])

#y_new = knn.predict(x_new)

#print(y_new)

###########################



x_train , x_test , y_train , y_test = train_test_split(iris.data, iris.target, test_size=0.3,
                                                       random_state=42,stratify=iris.target)


print(x_test.shape)


knn1 = KNeighborsClassifier(n_neighbors=5)
knn1.fit(x_train,y_train)
y_predict = knn1.predict(x_test)

print(y_predict)

print(knn1.score(x_test, y_test))


###########################