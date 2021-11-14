# -*- coding: utf-8 -*-
#k-means clustering

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

path="C:/Users/Danish/Desktop/python/kmeans/iris.csv"
iris=pd.read_csv(path)
print(iris)

#remove the y vairiable for clustering
iris.columns
iris=iris.drop(['type'],axis=1)

#create a numpy to do kmeans
cols=iris.columns
x=np.array(iris[cols].values)

#create an empty list to store the within clusters sum of clusters wcss
#plot the wcss to get the optimal number of clusters
wcss=[]

#start with 15 clusters, number of clusters to be as low as possible
num=np.arange(1,15)
#init used for the random initialization trap
for k in num:
	kmeans=KMeans(n_clusters=k,init='k-means++',max_iter=300,random_state=0).fit(x)
	#fit it onto the dataset
	wcss.append(kmeans.inertia_)
	
#plot the clusters
plt.plot(num,wcss)
plt.title('Clusters for iris')
plt.xlabel('Clsuters')
plt.ylabel('Errors')
plt.show()	

#based on the above elbow graph, the optimal clusters = 3
opt_k=3

#building the model
kmeans=KMeans(n_clusters=opt_k,init='k-means++',max_iter=400,random_state=1)
#using fit_predict because we're predicting the clusters on the same dataset
clusters=kmeans.fit_predict(x)
print(clusters)
iris['clusters']=clusters
print(iris)
iris.clusters.value_counts()

#plot the 3 clusters
iris.columns
#clusters based on petal length and petal width
plt.scatter(x[clusters==0,0],x[clusters==0,1],s=30,c='red',label='cluster 1')
plt.scatter(x[clusters==1,0],x[clusters==1,1],s=30,c='blue',label='cluster 2')
plt.scatter(x[clusters==2,0],x[clusters==2,1],s=30,c='green',label='cluster 1')






