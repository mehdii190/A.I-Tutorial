import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn import datasets



iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)



for data in range(len(df.columns)):
    print(data)
    sb.displot(df[df.columns[data]],kde_kws = {"color":"b","lw":3,"label":"KDE"})
    plt.tight_layout()
    
    
 
##############################


 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    