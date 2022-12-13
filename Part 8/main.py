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
