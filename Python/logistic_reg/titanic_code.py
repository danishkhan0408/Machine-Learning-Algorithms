# -*- coding: utf-8 -*-
#Logistic regression
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import classification_report as cr
from pandas_ml import ConfusionMatrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import recall_score, precision_score
path="F:/python/logistic_reg/train.csv"
df=pd.read_csv(path)
print(df)

#head/tail
df.head()
df.tail()

#in LR the Y-var must be numeric
#data types
df.dtypes

df.attr.value_counts()

df=df.drop(['PassengerId'],axis=1)
df=df.drop(['Name'],axis=1)
df=df.drop(['Ticket'],axis=1)

df.SibSp.value_counts()

#summary
df.describe()
df.shape

#EDA
#split into numeric and factor datatypes
num_cols=df.select_dtypes(include=['int32','int64','float32','float64']).columns
print(num_cols)

#check for nulls
df.isnull().sum()

df.Embarked.value_counts
df=df.drop(['Embarked'],axis=1)
df=df.drop(['Cabin'],axis=1)
df.isnull().sum()

#fixing the nulls
df.isnull().sum()
df.Age[df.Age.isnull()==True]=np.median(df.Age[df.Age.isnull()==False])

#check for zeros
df[num_cols][df[num_cols]==0].count()

#check for multicollinearity
cols=df[num_cols].columns
totalcols=len(cols)
cor=df[num_cols].corr()

#plot the heatmap
sns.heatmap(cor, xticklabels=cols[0:totalcols-1],yticklabels=cols[0:totalcols-1],annot=True,vmin=0,vmax=1,linewidth=0.5,square=True)

#parch and SibSp high multicollinearity


#convert the y-variable attrition into a number
'''
df.Sex.value_counts()
df['sex']=0
df.sex[df.Sex=="male"]=1
df=df.drop(['Sex'],axis=1)
'''

fact_cols=df.select_dtypes(include=['object']).columns
print(fact_cols)

#Male =1, Female = 0

#factors
for f in fact_cols:
	print('factor variables = {}'.format(f))
	print(df[f].unique())
	print("-----------------------")

sns.countplot('Sex',data=df,palette="hls")

#group by
groups = pd.DataFrame(df.groupby('Sex').mean())
groups[['Sex']]

#cross-tabulation
pd.crosstab(df.department,df.attr).plot(kind="bar")

#dummy variables
pd.get_dummies(df.Sex).head()
pd.get_dummies(df.Sex,drop_first=True).head()

#create a copy of the dataset
newdf=df.copy()

#convert the factors to dummy variables
for f in fact_cols:
	dummy=pd.get_dummies(df[f],drop_first=True,prefix=f)
	newdf=newdf.join(dummy)

len(df.columns)
print(df.columns)
#to remove the extra columns such as marital etc
newcols=df.columns
newcols=list(set(newcols).difference(set(fact_cols)))
len(newcols)
print(newcols)

#dataset with the new columns
df=df[newcols]
len(df.columns)
len(df.columns)

#readjust the y variable as the first or the last column
#drop the attr from the dataframe, the concat the attr at the end of the dataset
df=pd.concat([df.drop(['Survived'],axis=1),df['Survived']],axis=1)
df.columns

#split the data into training and testing
train,test=train_test_split(df,test_size=0.3)
print('train= {}, test= {}'.format(train.shape,test.shape))
totalcols=len(train.columns)

trainx=train.iloc[:,0:totalcols-1]
trainy=train.iloc[:,totalcols-1]
print('trainx= {}, trainy= {}'.format(trainx.shape,trainy.shape))

testx=test.iloc[:,0:totalcols-1]
testy=test.iloc[:,totalcols-1]
print('testx= {}, testy= {}'.format(testx.shape,testy.shape))

#build the logistic regression model
m1=sm.Logit(trainy,trainx).fit()
m1.summary()

#predictions
p1=m1.predict(testx)
p1[0:11]#contains the probabilities Max Likelihood

predy=p1.copy()

testy.value_counts()
c1=len(p1[p1<=0.3545])
c2=len(p1[p1>0.3545])
print("<= 0.5 are {}\n >0.5 are {}".format(c1,c2))

#convert into 0's and 1's
predy[predy<=0.3545]=0
predy[predy>0.3545]=1
predy.value_counts()

predy[predy<=0.5]=0
predy[predy>0.5]=1
predy.value_counts()



#confusion matrix
ConfusionMatrix(testy,predy)
predy.value_counts()

print(cr(testy,predy))

#print the ROC/AUC
from sklearn import metrics
fpr,tpr,threshold=metrics.roc_curve(testy,predy)
roc_auc=metrics.auc(fpr,tpr)

#plot the curve
plt.title('Reciever Operating Characteristics')
plt.plot(fpr,tpr,'b',label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([0,1])
plt.ylim([0,1])
plt.xlabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
















