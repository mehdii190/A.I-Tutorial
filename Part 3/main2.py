import numpy as np
import matplotlib.pyplot as plt


years=[1960,1970,1980,1990,2000,2010,2016]
iran_top=[21.91,32.2,34,54,66,78,89]
iraq_top=[21.91,32.2,34,50,60,77,86]
plt.xlabel('Year')
plt.ylabel('Populustion')
plt.plot(years,iran_top,ls='-',marker='o',mew=4)
plt.plot(years,iraq_top,ls='-',lw=1)
plt.show()