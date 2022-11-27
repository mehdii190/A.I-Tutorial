from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



iris = datasets.load_iris()

x_train , x_test , y_train , y_test = train_test_split(iris.data, iris.target, test_size=0.3,
                                                       random_state=42,stratify=iris.target)


knn = KNeighborsClassifier(5)
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)

print(y_predict)
print("################")
for i in y_predict:
    if not i:
        print(i, sep="\n")