import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


x = pd.read_csv('/Users/mehdimirawa/PycharmProjects/I.A.Class/smartphones.csv')
print(type(x))


#sb.stripplot(data=x,size=10)
#plt.show()

#################################

#sb.stripplot(y='Capacity',data=x,size=10)
#plt.show()


sb.stripplot(data=x,size=10)
plt.show()



#sb.stripplot(x='OS',y='Capacity',data=x,size=10)
#plt.show()





#y=x['Capacity']
#x=x['OS']
#plt.scatter(x,y)
#plt.show



#sb.swarmplot(x='OS',y='Capacity',data=x,size=10,hue='Company')
#plt.show()





#sb.boxplot(x='Company',y='Ram',data=x)
#plt.show()






#sb.jointplot(x='Company',y='Ram',data=x,kind='scatter')
#plt.show()




sb.pairplot(x,hue='Name',palette='hls')
plt.show()
