# -*- coding: utf-8 -*-
#ch12 Pandas
import numpy as np
import string
import random as r
import pandas as pd

#create a dictionary with the following:
#players : id, name, matches, runs, avg, age
pid=np.arange(1,101)
matches= np.random.randint(1,400,100)
runs= np.random.randint(1,15000,100)
avg=np.round(np.random.uniform(2,60,100),2)
age=np.random.randint(18,38,100)
string.ascii_letters
names = r.choices(string.ascii_letters,k=100) # where k is no of names

#create a dictionary
d_players={'PlayerID':pid,'Matches':matches,'Runs':runs,'Average':avg,'Age':age,'Name':names}
print(d_players)

#now converting dictionary into a dataframe/pandas

p_players=pd.DataFrame(d_players)
print(p_players)

#setting the index (and remove the default index)
p_players.set_index('PlayerID')

##setting the index and retain the column
p_players.set_index('PlayerID',drop=False)

#summarize the dataframe
p_players.describe()

#accessing the dataframe
p_players.head()
p_players.tail()
p_players[0:20]


#by colnames
p_players.Matches
max(p_players.Matches)
min(p_players.Matches)

#mulitple columns
p_players[['Name','Matches']]

#accessing a particular row
p_players[0:1] #to access the 1st row
p_players[23:24] #to access the 24th row

#calc the total runs
#p_players['Runs'].sum()
colname='Runs'
p_players[colname].sum()
#for the first 50 players
p_players[colname][0:50].sum()


#add a new column to the pandas
p_players['location']=None

#list of all columns
p_players.columns

#datatypes of all columns
p_players.dtypes

#add a new column awards adn initialize it with 0
p_players['awards']=0

#update record in pandas
country=['India']*20+['Aus']*20+['Pak']*20+['ENG']*20+['SA']*20
country
r.shuffle(country)
p_players['location']=country
p_players

#unique values of a given column
p_players.location.unique()

#queries
#select * from <> where name ='A'
p_players[p_players.Name=='A']

#selecting specific columns name, matches, runs where avg>40
p_players[['Name','Matches','Runs']][p_players.Average>=40]

#AND Condition
p_players[['Name','Matches','Runs']][(p_players.Matches>100) & (p_players.Average>40)]

#for all Indian players with a random numbers bw 5-10 matching the foll condition: avg>35, matches>25
p_players[(p_players.location == 'India') & (p_players.Matches>25) & (p_players.Average>35)]=r.randint(5,10)

p_players[['Name','Matches','Runs','awards']][(p_players.location=='India') & (p_players.Matches>25) & (p_players.Average>35)]


#OR Condition
p_players[['Name','Matches','Runs']][(p_players.Matches>100) | (p_players.Average>40)]


#drop unwanted columns from a panda
p_players['gender']=None
p_players["height"]=None
p_players["weight"]=None
p_players
p_players=p_players.drop(['gender'],axis=1) #here axis = 1 for columns axis = 0 for rows

#dropping multiple columns
p_players=p_players.drop(['height','weight'],axis=1)
p_players

#EDA on pandas
#check for zeros
if(len(p_players.Runs[p_players.Runs==0])>0):
	print("Zeros present")
else: print("No zeros")

#check for nulls
if(len(p_players.Runs[p_players.Runs.isnull()])>0):
	print("nulls present")
else: print("No nulls")

#generalized code
cols=p_players.columns
print(cols)
for c in cols:
		if(len(p_players[c][p_players[c]==0])>0):
			print(c+" has Zeros")
		else: print(c+" has no zeros")
		#check for nulls
		if(len(p_players[c][p_players[c].isnull()])>0):
			print(c+" has nulls present\n")
		else: print(c+" has no nulls\n")

#read a csv file
path="C:/Users/Danish/Desktop/Data science/linear reg/concrete.csv"
conc=pd.read_csv(path)
print(conc)

#writing pandas dataframe into csv file
p_players.to_csv("playerz.csv")
import os
os.getcwd()



