# -*- coding: utf-8 -*-

#Comparision between linear, decision trees and random forest
import pandas as pd
import numpy as np
import statsmodels.api as sms
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

from sklearn.tree import DecisionTreeRegressor as dtr
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestRegressor as rfr

path="C:/Users/Danish/Desktop/python/compare/concrete.csv"
conc=pd.read_csv(path)
print(conc)

#head/tail
conc.head()
conc.tail()

#data types
conc.dtypes
conc.columns

#summary
conc.describe()

#check for nulls
conc.isnull().sum()

#check for zeros
conc[conc==0].count()

#other checks: multicollinearity etc

#train and test split
totalcols=len(conc.columns)
x=conc.iloc[:,0:totalcols-1]
y=conc.iloc[:,totalcols-1]
trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.3)

print(trainx.shape,trainy.shape)
print(testx.shape,testy.shape)

#build the models
#1) Linear Regression- Ordinary Least Square (OLS) method
m1=sms.OLS(trainy,trainx).fit()
p1=m1.predict(testx)
#2) Decision Tree: MSE model for Linear Regression
m2=dtr(criterion="mse",max_depth=5,min_samples_leaf=3).fit(trainx,trainy)
p2=m2.predict(testx)
#3) Random Forest
m3=rfr().fit(trainx,trainy)
p3=m3.predict(testx)

#create a dataframe to store the actual and the predicted results
df=pd.DataFrame({'Actual':testy,'LINEAR':p1,'DT':p2,'RF':p3})
print(df)

SSE1 = sum(np.square(df['Actual']-df['LINEAR']))
MSE1 = sum(np.square(df['Actual']-df['LINEAR']))/len(df)

SSE2 = sum(np.square(df['Actual']-df['DT']))
MSE2 = sum(np.square(df['Actual']-df['DT']))/len(df)

SSE3 = sum(np.square(df['Actual']-df['RF']))
MSE3 = sum(np.square(df['Actual']-df['RF']))/len(df)

print("SSE for Linear Regression =",SSE1)
print("SSE for Decision Trees =",SSE2)
print("SSE for Random Forest =",SSE3)


print("MSE for Linear Regression =",MSE1)
print("MSE for Decision Trees =",MSE2)
print("MSE for Random Forest =",MSE3)










