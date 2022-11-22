############## imports ###############

from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import string
import sklearn
import csv


####################################

### dataSet ###

data = pd.read_csv('/Users/mehdimirawa/Desktop/video IA/spam.csv', encoding='latin-1')
#print(data.shape)
#print(data.info())

####################################


data = data.drop(["Unnamed: 2", "Unnamed: 3","Unnamed: 4"], axis=1)
data = data.rename(columns={"v2": "text", "v1": "label"})

print(data.shape)
print(data.info())

###################################


print(data["label"].value_counts())





