# -*- coding: utf-8 -*-
#KNN - regressor
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from pandas_ml import ConfusionMatrix
from sklearn.metrics import classification_report as cr
from sklearn.metrics import mean_squared_error as mse


path="C:/Users/Danish/Desktop/python/compare/concrete.csv"
conc=pd.read_csv(path)
print(conc)

#convert the features into a standardized form
#use minmax:
#MinMax = [x - min(x)] / [max(x) - min(x)]
conc_scale=conc.copy()
minmax=preprocessing.MinMaxScaler()
totalcols=len(conc_scale.columns)
scaledvals=minmax.fit_transform(conc_scale.iloc[:,0:totalcols-1])
conc_scale.iloc[:,0:totalcols-1]=scaledvals

#shuffle the dataset
conc_scale=conc_scale.sample(frac=1)

#train and test split
totalcols1=len(conc_scale.columns)
x=conc_scale.iloc[:,0:totalcols1-1]
y=conc_scale.iloc[:,totalcols1-1]
trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.3)

print(trainx.shape,trainy.shape)
print(testx.shape,testy.shape)

#to get the minimum SSE
sse_scores=[]
for k in range(1,21):
	knn=neighbors.KNeighborsRegressor(n_neighbors=k).fit(trainx,trainy)
	pred=knn.predict(testx)
	err=mse(testy,pred).mean()
	sse_scores.append(err)

print(sse_scores)
print(min(sse_scores))
opt_k=sse_scores.index(min(sse_scores))+1

#build the model
m1=neighbors.KNeighborsRegressor(n_neighbors=opt_k).fit(trainx,trainy)
p1=m1.predict(testx)

#create a dataframe to store the actual and the predicted results
df=pd.DataFrame({'actual':testy,'predicted':p1})
print("SSE = {}".format(sum(np.square(df['actual']-df['predicted']))))
print("MSE = {}".format(sum(np.square(df['actual']-df['predicted']))/len(df)))

print(df)


