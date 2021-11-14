# -*- coding: utf-8 -*-

#PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.decomposition import PCA

path="C:/Users/Danish/Desktop/python/bodyfat.csv"
body_fat = pd.read_csv(path)
#split as x and y variables
body_fat_x=body_fat.iloc[:,1:11]
body_fat_y=body_fat.iloc[:,0]

#for scaler: (x-mean)/std deviation
# mean =0 and sd=1
#data becomes unitless for both scaler and minmax
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(body_fat_x)
scaled_body_fat_x=scaler.transform(body_fat_x)

pca= decomposition.PCA()
pca.fit(scaled_body_fat_x)

body_fat_x_pca1=pca.transform(scaled_body_fat_x)

pca.explained_variance_ratio_

pca.explained_variance_ratio_.sum()

#orthogonal trasnformation has been completed
#axis rotation has been done (here 9 dimensions are there)
body_fat_x_pca1
#first 3 give the most (85%) of variance of data
#forst 5 principle components explains 90% variance of the data
#the last one explains 0.2% od variance
#but the axis has been rotated but it doesnt mean that age has been mapped to the highest value of variance explanation.
#if the columns are changd the values of variance will be the same
#hence cannot be used for feature selection
body_fat_x_pca1.shape
#check the multicollinearity
check=pd.DataFrame(body_fat_x_pca1).corr()


from sklearn import linear_model

lcn_model = linear_model.LinearRegression()

body_fat_x_pca1_df=pd.DataFrame(body_fat_x_pca1)
#selecting the first 4 principle components
lcn_model.fit(body_fat_x_pca1_df.iloc[:,[0,1,2,3]]  ,  body_fat_y)

lcn_model.coef_
lcn_model.score(body_fat_x_pca1_df.iloc[: , [0,1,2,3]],body_fat_y)

import statsmodels.api as sm #Linear regression library
m1=sm.OLS(body_fat_y, body_fat_x_pca1_df.iloc[:,[0,1,2,3]]).fit()

#summarize the model
m1.summary()