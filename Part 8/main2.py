import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as sbfrom sklearn.preprocessing import StandardScaler, normalizefrom sklearn.cluster import KMeans#from sklearn.decompostion import PCA##########################creditcards = pd.read_csv("/Users/mehdimirawa/Desktop/video IA/marketing_data.csv")print(creditcards.head())print(creditcards.info())describe = creditcards.describe()##########################mx = creditcards["BALANCE"].max()full_max=creditcards[creditcards["BALANCE"]==mx]##########################a=creditcards.isnull().sum()print(creditcards.isnull().sum())##########################creditcards["MINIMUM_PAYMENTS"].fillna(creditcards["MINIMUM_PAYMENTS"].mean(),inplace=True)creditcards["CREDIT_LIMIT"].fillna(creditcards["CREDIT_LIMIT"].mean(),inplace=True)print(creditcards.isnull().sum())##########################creditcards.drop("CUST_ID",axis=1,inplace=True)print(creditcards.head)###########################plt.figure(figsize=)sb.distplot(creditcards[creditcards.columns[0]],kde_kws = {"color":"b","lw":3,"label":"KDE"},hist_kws={"color":"g"})plt.tight_layout()###########################plt.subplots(figsize=(20,10))sb.heatmap(creditcards.corr(),annot=True)plt.show()###########################scores = []for i in range(1,10):    kmn = KMeans(n_clusters=i)    kmn.fit(creditcards)    scores.append(kmn.inertia_)    ##########################scaler= StandardScaler()creditcards_scaled = scaler.fit_transform(creditcards)######new_kmn = KMeans(n_clusters=8)new_kmn.fit(creditcards_scaled)#label = new_kmn.predict(creditcards_scaled)label2 = new_kmn.labels_centriods = new_kmn.cluster_centers_###########################cluster_centerss = scaler.inverse_transform(new_kmn.cluster_centers_)cluster_centerss = pd.DataFrame(data=cluster_centerss,columns=[creditcards.columns])#############################final_cluster = pd.concat([creditcards,pd.DataFrame({"cluster":label2})],axis=1)for x in creditcards.columns:    plt.figure(figsize = (35,5))    for y in range(7):        plt.subplot(1,7,y+1)        cluster = final_cluster[final_cluster["cluster"]==y]        cluster[x].hist(bins = 20)        plt.title("{} \nCluster {}".format(x,y))