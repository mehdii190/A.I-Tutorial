from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib as plt


iris = datasets.load_iris()


##########################

print(iris.data.shape)
print(iris.feature_names)

##########################



iris_df = pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df['target']=iris.target


###########################

#pd.plotting.scatter_matrix(iris_df,c=iris.target)

