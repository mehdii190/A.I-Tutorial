import sklearn
from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/persian computer/Desktop/website/I.A-Tutorial/smartphones.csv")


def plot_box(df1, ft):
    df1.boxplot(column=[ft])
    plt.grid(False)
    plt.show()


plot_box(df, "Ram")


def outlier(df1, ft):
    Q1 = df1[ft].quantile(0.25)
    Q3 = df1[ft].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 + IQR
    upper = Q3 + 1.5 - IQR

    ls = df.index[(df[ft] < lower) | (df[ft] > upper)]

    return ls


list_index = []

for ram in ['Ram']:
    list_index.extend(outlier(df, ram))


def remove(df1, ls):
    ls = sorted(set(ls))
    df1 = df.drop(ls)
    return df1


df_removed = remove(df, ram)

df_removed.shape



