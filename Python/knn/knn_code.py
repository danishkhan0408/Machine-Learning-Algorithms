# -*- coding: utf-8 -*-
#KNN
#k is the number of neighbours
#k usually in the range of 3 to 11
#and k is an odd number
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from pandas_ml import ConfusionMatrix
from sklearn.metrics import classification_report as cr

path="C:/Users/Danish/Desktop/python/knn/wheat.csv"
wheat=pd.read_csv(path)
print(wheat)
wheat.dtypes

#convert the features into a standardized form
#use minmax:
#MinMax = [x - min(x)] / [max(x) - min(x)]
wheat_scale=wheat.copy()
minmax=preprocessing.MinMaxScaler()
totalcols=len(wheat_scale.columns)
scaledvals=minmax.fit_transform(wheat_scale.iloc[:,0:totalcols-1])
wheat_scale.iloc[:,0:totalcols-1]=scaledvals

#shuffle the dataset
wheat_scale=wheat_scale.sample(frac=1)

#get the count of the classes
wheat_scale.type.value_counts()

#train and test split
totalcols1=len(wheat_scale.columns)
x=wheat_scale.iloc[:,0:totalcols1-1]
y=wheat_scale.iloc[:,totalcols1-1]
trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.25)

print(trainx.shape,trainy.shape)
print(testx.shape,testy.shape)

#cross validation to select the optimal neighbors
nn=list(range(3,12,2))
nn
cv_score=[]

for k in nn:
	knn=neighbors.KNeighborsClassifier(n_neighbors=k)
	scores=cross_val_score(knn,trainx,trainy,cv=5,scoring="accuracy")
	#cv = no of folds and scoring mechanism is accuracy
	cv_score.append(scores.mean())

#to get max accuracy
print(cv_score)
print(max(cv_score))
cv_score.index(max(cv_score))#index of max
opt_k=nn[cv_score.index(max(cv_score))]#optimum k

#model building
m1=neighbors.KNeighborsClassifier(n_neighbors=opt_k).fit(trainx,trainy)
p1=m1.predict(testx)
ConfusionMatrix(list(testy),list(p1))
#overall accuracy
print(accuracy_score(testy,p1))

#classification report
print(cr(testy,p1))

