import matplotlib.pyplot as plt
import pandas as pd


txt = pd.read_csv('text.txt')
plt.plot(txt)