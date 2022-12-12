import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
#################
X = [1,2,3,4,5]
Y = [1,2,1.3,3.75,2.25]
#################
plt.scatter(X,Y)
plt.plot()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
######## mean x , y #######
x_mean = np.mean(X)
y_mean = np.mean(Y)
######## VAR #########
var = np.var(X, ddof=1)
######## COV #########
n = 5
nn = 2
cov = np.zeros((nn,nn))
xm = np.stack([X,Y])
for i in range(nn):
    for j in range(nn):
        x1 = xm[i,:]
        x2 = xm[j,:]
        x1_mean = x1.mean()
        x2_mean = x2.mean()
        for k in range(5):
            cov[i,j]+=(x1[k]-x1_mean)*(x2[k]-x2_mean)
        cov[i,j]/=n-1
print(cov)
########## or cov np
cov2 = np.cov(X,Y, ddof=1)
########## b ######
b = cov / var
########## a #######
a = y_mean / b*x_mean




























