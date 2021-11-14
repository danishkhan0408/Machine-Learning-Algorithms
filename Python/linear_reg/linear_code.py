# -*- coding: utf-8 -*-
#Linear Regression
import pandas as pd
import numpy as np
import statsmodels.api as sm #Linear regression library
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt #inbuilt visualization package
import seaborn as sns #visualization package
import scipy.stats as stats

path="C:/Users/Danish/Desktop/python/linear_reg/energy_cooling_load.csv"
energy=pd.read_csv(path)
print(energy)

#head/tail
energy.head()
energy.tail()

#data type
energy.dtypes

#summary
energy.describe()

#column list
energy.columns

#check for nulls
energy.isnull().sum()

#check for zeros
energy[energy==0].count()

#update the NULLs with the mean value
#energy.surf_area[energy.surf_area.isnull()]="0"
#energy.surf_area[energy.surf_area == '?']="0"
#energy.surf_area=energy.astype('float64',copy=False)
#sa_mean=np.mean(energy.surf_area[energy.surf_area > 0])

#check for singularities
#equivalent to table function in R
energy.over_ht.value_counts()
energy.orient.value_counts()

#EDA
#check for distributions
sns.distplot(energy.rel_comp)
sns.distplot(energy.wall_area)

#to get all the charts in one page
cols=energy.columns
len(cols)
r=3;c=3;pos=1

fig=plt.figure() #create an instace of figure( ) class and returns a blank chart
for e in cols:
	fig.add_subplot(r,c,pos)
	sns.distplot(energy[e])
	pos+=1

#check for outliers
energy.boxplot("wall_area",vert=False)

cols=energy.columns
r=3;c=3;pos=1
fig=plt.figure()
for e in cols:
	fig.add_subplot(r,c,pos)
	energy.boxplot(e,vert=False)
	pos+=1
	
#check for multicollinearity
totalcols=len(cols)
cor=energy.iloc[:,0:totalcols-1].corr()

#plot the heatmap
sns.heatmap(cor, xticklabels=cols[0:totalcols-1],yticklabels=cols[0:totalcols-1],annot=True,vmin=0,vmax=1,linewidth=0.5,square=True)

#split hte data into train and test
#in pythone the data is split into train and test
#eg: total rows=1000, cols=10
#train= rows=700, cols=10 and test: rows=300, cols=10
#train is subdivided into trainx and train y
#trainx: rows= 700, cols=9 and trainy: rows=700 and cols=1 (the y variable)
#similarly  test is also split into test x adn test y

train,test=train_test_split(energy,test_size=0.3)
print('train = {}, test = {}'.format(train.shape,test.shape))

#split the train data into trainx and train y
trainx=train.iloc[:,0:totalcols-1]
trainy=train.iloc[:,totalcols-1]
print('trainx = {}, trainy = {}'.format(trainx.shape,trainy.shape))

#split the test data into testx and test y
testx=test.iloc[:,0:totalcols-1]
testy=test.iloc[:,totalcols-1]
print('testx = {}, testy = {}'.format(testx.shape,testy.shape))


#building the Linear Regression model (OLS-Ordinary least Square model)
#in simple linear reg model, the summary cannot be dsiplayed
#in OLS model, the summary can be displayed
#also in OLS method the intercept is not present and has to be added manually beforehand

#add a the constant to trainx and testx
trainx=sm.add_constant(trainx)
testx=sm.add_constant(testx)

#building the Linear Regression ols model
m1=sm.OLS(trainy,trainx).fit()

#summarize the model
m1.summary()

#validation of the assumptions
#1) mean residuals=0
p1=m1.predict(trainx)
residuals=trainy-p1
print(np.mean(residuals))

#2) residuals have constant variance
sns.set(style="whitegrid")
sns.residplot(residuals,trainy,lowess=True,color="r")

#breusch pagan test
import statsmodels.stats.api as sms
bptest=sms.het_breuschpagan(m1.resid,m1.model.exog)
print("p-value from BP Breusch Pgan test : {}".format(bptest[1]))


#residuals have a normal distribution
import pylab
stats.probplot(residuals,dist="norm",plot=pylab)
pylab.show

#fix all the data by log transformations or boxcox or square root transformation, etc.

#log transformation
energy.cold_load=np.log2(energy.cold_load)
cols=energy.columns
len(cols)
r=3;c=3;pos=1
fig=plt.figure() #create an instace of figure( ) class and returns a blank chart
for e in cols:
	fig.add_subplot(r,c,pos)
	sns.distplot(energy[e])
	pos+=1

#predict
p1=m1.predict(testx)
len(p1)

#create a dataframe to store the actual and the predicted results
df=pd.DataFrame({'actual':testy,'predicted':p1})
df.head()
print("SSE = {}".format(sum(np.square(df['actual']-df['predicted']))))
print("MSE = {}".format(sum(np.square(df['actual']-df['predicted']))/len(df)))

#feature selection
e2=energy.copy()
e2=energy.drop(['orient'],axis=1)
e2.columns






