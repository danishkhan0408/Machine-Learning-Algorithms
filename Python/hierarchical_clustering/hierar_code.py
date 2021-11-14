# -*- coding: utf-8 -*-
#Hierarchical clustering

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering as agc

path="C:/Users/Danish/Desktop/python/hierarchical_clustering/mallcustomers.csv"
mall=pd.read_csv(path)

mall.columns
#perform teh null check
#taking 'annual income' and 'spending score' columns
x=mall.iloc[:,3:5].values

#find the optimum number of clsuters required by plotting the dendogram
#repeat the procedure for all other columns
dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('customers')
plt.ylabel('distances')
plt.show()

#based on the dendrogram optimum clsuters=5
#build the hierarchical clustering model
opt_clust=5
hc=agc(n_clusters=opt_clust,affinity="euclidean",linkage='ward').fit_predict(x)
print(hc)

#associate every cluster with the dataset
mall['clusters']=hc
mall.clusters.value_counts()

#visualize the clusters
#s= size of the dots
plt.scatter(x[hc==0,0],x[hc==0,1],s=30,c='red',label='c1')
plt.scatter(x[hc==1,0],x[hc==1,1],s=30,c='blue',label='c2')
plt.scatter(x[hc==2,0],x[hc==2,1],s=30,c='green',label='c3')
plt.scatter(x[hc==3,0],x[hc==3,1],s=30,c='violet',label='c4')
plt.scatter(x[hc==4,0],x[hc==4,1],s=30,c='black',label='c5')
plt.xlabel('customers')
plt.ylabel('Income')
plt.title('Cluster of customers')
plt.legend()
plt.show()





