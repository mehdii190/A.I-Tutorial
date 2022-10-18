import numpy as np
import matplotlib.pyplot as plt

years=[1960,1970,1980,1990,2000,2010,2016]
iran_top=[21.91,32.2,34,54,66,78,89]
#plt.plot(years,iran_top)
#plt.show()

#plt.figure(figsize=(10,6),dpi=50)
#plt.plot(years,iran_top)
#plt.show()

#plt.xlabel('Year')
#plt.ylabel('population')
#plt.plot(years,iran_top)
#plt.show()


#plt.xlabel('Year')
#plt.ylabel('population')
#plt.plot(years,iran_top)
#plt.xticks(years)
#plt.show()


plt.xlabel('Year')
plt.ylabel('population')
plt.plot(years,iran_top,ls='-',marker='x',mew=4)
plt.show()



