import numpy as np
import matplotlib.pyplot as plt


#years=[1960,1970,1980,1990,2000,2010,2016]
#iran_top=[21.91,32.2,34,54,66,78,89]
#iraq_top=[21.91,32.2,34,50,60,77,86]
#plt.xlabel('Year')
#plt.ylabel('Populustion')
#plt.plot(years,iran_top,ls='-',marker='o',mew=4)
#plt.plot(years,iraq_top,ls='-',lw=1)

#plt.legend(['iran','iraq'],loc='best')
#plt.grid()
#plt.show()



#####################################


#years=[1960,1970,1980,1990,2000,2010,2016]
#iran_top=[21.91,32.2,34,54,66,78,89]
#plt.scatter(years,iran_top,s=40)
#plt.annotate('here',(1980,34))
#plt.show()


############################

#years=np.arange(7)
#iran_top=[21.91,32.2,34,54,66,78,89]
#plt.scatter(years,iran_top)
#plt.show()

############################

#years=np.arange(7)
#iran_top=[21.91,32.2,34,54,66,78,89]
#plt.scatter(years,iran_top,c='red')
#plt.title('iran pop')
#plt.show()



#########################

#years=np.arange(7)
#iran_top=[21.91,32.2,34,54,66,78,89]
#x=np.array(iran_top)
#plt.scatter(years,iran_top,c='red',s=x/20)
#plt.title('iran pop')
#plt.show()


########################

#years=np.arange(7)
#iran_top=[21.91,32.2,34,54,66,78,89]
#plt.scatter(years,iran_top,c='red')
#plt.title('iran pop')
#plt.margins(0.3)
#plt.show()

#######################


#city_name=['tehran','mashad','rasht']
#city_top=[21,19,15]
#plt.title('iran pop')
#plt.hist(city_top)
#plt.show()

########################


#city_name=['tehran','mashad','rasht']
#city_top=[21,19,15]
#plt.hist(city_top,bins=2)
#plt.show()


#########################


#city_name=['tehran','mashad','rasht']
#city_top=[21,19,15]
#plt.pie(city_top,labels=city_name)
#plt.show()


##########################

years = np.arange(7)
iran_top=[21.91,32.2,34,54,66,78,89]
iraq_top=[21.91,32.2,34,50,60,77,86]

plt.subplot(1,2,1)
plt.plot(years,iran_top)

plt.subplot(1,2,2)
plt.plot(years,iraq_top)
plt.show()

