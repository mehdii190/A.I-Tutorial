import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame(np.array([1, 2, 3, 4, 10, 27]))
print('Q1= ',df.quantile(0.25))
print('Q2= ',df.quantile(0.5))
print('Q3= ',df.quantile(0.75))


df.boxplot()
plt.show()