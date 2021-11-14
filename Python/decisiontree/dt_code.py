# -*- coding: utf-8 -*-
#Decision Tree
#it is a part of CART - CLassification and Regression Technique

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report as cr
from sklearn.feature_selection import RFE #Recursive Feature Elimination
from pandas_ml import ConfusionMatrix
import seaborn as sns
from IPython.display import Image
from io import StringIO
import pydotplus


path="C:/Users/Danish/Desktop/python/decisiontree/ecoli.csv"
ecoli=pd.read_csv(path)
print(ecoli)

#head/tail
ecoli.head()
ecoli.tail()

#data types
ecoli.dtypes

#column names
ecoli.columns
#remove the name
ecoli=ecoli.drop(['sequence_name'],axis=1)

#check for multicollinearity
num_cols=ecoli.select_dtypes(include=['float64']).columns
cols=ecoli[num_cols].columns
totalcols=len(cols)
cor=ecoli[num_cols].corr()

#plot the heatmap
sns.heatmap(cor, xticklabels=cols[0:totalcols-1],yticklabels=cols[0:totalcols-1],annot=True,vmin=0,vmax=1,linewidth=0.5,square=True)

#count the number of classes
ecoli.lsp.value_counts()
ecoli.lsp.value_counts().sum()

#shuffle the dataset
ecoli=ecoli.sample(frac=1)

#split the data into training and testing
train,test=train_test_split(ecoli,test_size=0.3)
print('train= {}, test= {}'.format(train.shape,test.shape))

#check for the distribution pf classes in train adn test
train.lsp.value_counts()
test.lsp.value_counts()

totalcols=len(train.columns)
trainx=train.iloc[:,0:totalcols-1]
trainy=train.iloc[:,totalcols-1]
print('trainx= {}, trainy= {}'.format(trainx.shape,trainy.shape))

testx=test.iloc[:,0:totalcols-1]
testy=test.iloc[:,totalcols-1]
print('testx= {}, testy= {}'.format(testx.shape,testy.shape))



########################################################################################################################
#model building

#1) Entropy model
#random state is like set.seed() to get the saem results
m_entropy=dtc(criterion="entropy",max_depth=4,random_state=100,min_samples_leaf=2).fit(trainx,trainy)

#view the decision tree
out_data=StringIO()
tree.export_graphviz(m_entropy,out_file=out_data,filled=True,rounded=True,special_characters=True, feature_names=cols[0:totalcols-1],class_names=ecoli.lsp.unique())
graph=pydotplus.graph_from_dot_data(out_data.getvalue())

Image(graph.create_png())
#prediction
p_entropy=m_entropy.predict(testx)

#confusion matrix
ConfusionMatrix(list(testy),list(p_entropy))
testy.value_counts()

#overall accuracy
print(accuracy_score(testy,p_entropy))

#classification report
print(cr(testy,p_entropy))

########################################################################################################################

#2) GINI model
#random state is like set.seed() to get the saem results
m_gini=dtc(criterion="gini",max_depth=4,random_state=100,min_samples_leaf=2).fit(trainx,trainy)

#view the decision tree
out_data=StringIO()
tree.export_graphviz(m_gini,out_file=out_data,filled=True,rounded=True,special_characters=True, feature_names=cols[0:totalcols-1],class_names=ecoli.lsp.unique())
graph=pydotplus.graph_from_dot_data(out_data.getvalue())

Image(graph.create_png())
#prediction
p_gini=m_gini.predict(testx)

#confusion matrix
ConfusionMatrix(list(testy),list(p_gini))
testy.value_counts()

#overall accuracy
print(accuracy_score(testy,p_gini))

#classification report
print(cr(testy,p_gini))
########################################################################################################################

#feature selection by RFE: Recursive Feature Elimination
#select the top 'n' features
n=5
rfe=RFE(m_gini,n).fit(testx,testy)
support=rfe.support_
ranking=rfe.ranking_

#store these features and ranks in a dataframe
df_rfe=pd.DataFrame({'columns':cols[0:totalcols-1],'support':support, 'ranking':ranking})
print(df_rfe)

########################################################################################################################

#ASSIGNMENT

#feature selection based on multicollinearity etc and create another set of models

#create a function to build the model
#building, confusion matrix,classification report, and accuracy score and return these values to the calling function (dont print inside the function)

#create a function to identify the important features by RFE (return the dataframe that holds the important features)






























