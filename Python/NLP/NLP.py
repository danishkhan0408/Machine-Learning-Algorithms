# -*- coding: utf-8 -*-
#by Pranjal Mishra
#Natural Language Processing : uses DT or RF
import pandas as pd
import numpy as np
#natural loanguage toolkit
import nltk
import matplotlib.pyplot as plt

path="C:/Users/Danish/Desktop/python/spam1.csv"
#can use encoding='cp1252' in read_csv
messages= pd.read_csv(path)

messages.head()
messages.shape
#6776 by 5

#converting to 2 columns only
messages=messages.iloc[:,[0,1]]
messages.shape
#rename the column names
messages.rename(columns={"v1":"label","v2":"message"},inplace=True)
messages.head()

#length of each message
length= messages.message.apply(len)
length
len(length) 

#add length to dataframe as a new column
messages= pd.concat([messages,length],axis=1)
messages.columns.values[2]="Length"

messages.label.replace({"ham":0,"spam":1},inplace=True)

#everything to lowercase or uppercase
messages.message=messages.message.str.lower()

from nltk.corpus import stopwords
import string
#nltk.download("stopwords")

#to see the stopwords
stopwords.words("english") #for english stopwrods, can use any other language

#to see the punctuations
string.punctuation

#_______________________________________________
#example
abc="i want to ? remove all !! all the ... punctuation marks $ from %%"
abc_refined=[i for i in abc if i not in string.punctuation]
abc_refined
#to convert back to sentence
abc_refined="".join(abc_refined)
#________________________________________________

#creating a function based the above example
def text_process(mess):
    """
    1.remove the punctuation
    2.remove the stopwords
    3. return the list of clean textwords
    """
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc="".join(nopunc)
    return [word for word in nopunc.split() if word not in stopwords.words("english")]

messages['message'].apply(text_process)


#to give the count of each 
from sklearn.feature_extraction.text import CountVectorizer    

bow_transformer = CountVectorizer(analyzer = text_process).fit(messages["message"])
#display the count of each word
bow_transformer.vocabulary_
#number of unique words
len(bow_transformer.vocabulary_)

#convert to Term Document Matrix
messages_bow= bow_transformer.transform(messages.message)
#term document model has been created
messages_bow.shape

from sklearn.model_selection import train_test_split
#split the TDM and y var is messages.label (ham and spam), random state is like set.seed
x_train, x_test, y_train, y_test = train_test_split(messages_bow, messages.label, test_size =0.2, random_state =100)

#using NaiveBayes classification
#can use Decision Tree and Random Forest
from sklearn.naive_bayes import MultinomialNB
naive_bay = MultinomialNB()

spam_nb= naive_bay.fit(x_train,y_train)
pred = naive_bay.predict(x_test)

from sklearn.metrics import confusion_matrix
tab = confusion_matrix(pred, y_test)
#to print the accuracy
tab.diagonal().sum() /  tab.sum() * 100

