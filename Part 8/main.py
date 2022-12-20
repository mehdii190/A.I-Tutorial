from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###########################
iris = datasets.load_iris()
###########################

kmn = KMeans(n_clusters=3)
kmn.fit(iris.data)
labels = kmn.predict(iris.data)

###########################

centriods = kmn.cluster_centers_

###########################

xs = iris.data[:,0]
ys = iris.data[:,1]
plt.scatter(xs, ys, c=labels)
plt.scatter(centriods[:,0],centriods[:,1],marker="x",s=150)
plt.show()

###########################

print(kmn.inertia_)

###########################

list_inerstia = []

for i in np.arange(1,7):
    kmn = KMeans(n_clusters=i)
    kmn.fit(iris.data)
    list_inerstia.append(kmn.inertia_)
print(list_inerstia)


plt.plot(np.arange(1,7), list_inerstia,"ro-")
plt.xlabel("number of clusters")
plt.ylabel("inertia")
plt.show()









