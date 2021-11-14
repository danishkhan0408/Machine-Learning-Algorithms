# -*- coding: utf-8 -*-
#Logistic regression
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import classification_report as cr
from pandas_ml import ConfusionMatrix
import matplotlib.pyplot as plt
import seaborn as sns

path="C:/Users/Danish/Desktop/python/logistic_reg/hr_emp.csv"
employee=pd.read_csv(path)
print(employee)

#head/tail
employee.head()
employee.tail()

#in LR the Y-var must be numeric
#data types
employee.dtypes

#convert the y-variable attrition into a number
employee['attr']=0
employee.attr[employee.attrition=="Yes"]=1
employee.attr.value_counts()

employee=employee.drop(['attrition'],axis=1)

#summary
employee.describe()
employee.shape

#distribution of classes
employee.attrition.value_counts()
employee.attr.value_counts()

#EDA
#split into numeric and factor datatypes
num_cols=employee.select_dtypes(include=['int32','int64','float32','float64']).columns
print(num_cols)
fact_cols=employee.select_dtypes(include=['object']).columns
print(fact_cols)

#check for nulls
employee.isnull().sum()

#check for zeros
employee[num_cols][employee[num_cols]==0].count()

#check for multicollinearity
cols=employee[num_cols].columns
totalcols=len(cols)
cor=employee[num_cols].corr()

#plot the heatmap
sns.heatmap(cor, xticklabels=cols[0:totalcols-1],yticklabels=cols[0:totalcols-1],annot=True,vmin=0,vmax=1,linewidth=0.5,square=True)

#factors
for f in fact_cols:
	print('factor variables = {}'.format(f))
	print(employee[f].unique())
	print("-----------------------")

#rename the levels in the factors to shorter names
employee.travel[employee.travel=="Travel_Rarely"]="rarely"
employee.travel[employee.travel=="Travel_Frequently"]="frequently"
employee.travel[employee.travel=="Non-Travel"]="no"

employee.department[employee.department=="Research & Development"]="rnd"
employee.department[employee.department=="Sales"]="sales"
employee.department[employee.department=="Human Resources"]="hr"

for f in fact_cols:
	print('factor variables = {}'.format(f))
	print(employee[f].unique())
	print("-----------------------")

sns.countplot('attr',data=employee,palette="hls")

#group by
groups = pd.DataFrame(employee.groupby('attr').mean())
groups[['age']]
groups[['age','distance','num_comp']]
groups[['yrs_since_prom']]

#cross-tabulation
pd.crosstab(employee.department,employee.attr).plot(kind="bar")

#dummy variables
pd.get_dummies(employee.department).head()
pd.get_dummies(employee.department,drop_first=True).head()

#create a copy of the dataset
newemp=employee.copy()

#convert the factors to dummy variables
for f in fact_cols:
	dummy=pd.get_dummies(employee[f],drop_first=True,prefix=f)
	newemp=newemp.join(dummy)

len(newemp.columns)
print(newemp.columns)
#to remove the extra columns such as marital etc
newcols=newemp.columns
newcols=list(set(newcols).difference(set(fact_cols)))
len(newcols)
print(newcols)

#dataset with the new columns
newemp=newemp[newcols]
len(employee.columns)
len(newemp.columns)

#readjust the y variable as the first or the last column
#drop the attr from the dataframe, the concat the attr at the end of the dataset
newemp=pd.concat([newemp.drop(['attr'],axis=1),newemp['attr']],axis=1)
newemp.columns

#split the data into training and testing
train,test=train_test_split(newemp,test_size=0.3)
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
c1=len(p1[p1<=0.5])
c2=len(p1[p1<0.5])
print("<= 0.5 are {}\n >0.5 are {}".format(c1,c2))

#convert into 0's and 1's
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

















