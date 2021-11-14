# -*- coding: utf-8 -*-
#Ch12: Pandas cotd
import pandas as pd
import numpy as np
import string
import random as r
path="F:/python/intro/playerz.csv"
players=pd.read_csv(path)
print(players)

#create another data frame
pid=np.arange(101,126)
matches= np.random.randint(10,120,25)
runs= np.random.randint(1,15000,25)
avg=np.round(np.random.uniform(2,60,25),2)
age=np.random.randint(18,38,25)
string.ascii_letters
names = r.choices(string.ascii_letters,k=25) # where k is no of names

#create a dictionary
d_players1={'PlayerID':pid,'Matches':matches,'Runs':runs,'Average':avg,'Age':age,'Name':names}
#print(d_players1)

#now converting dictionary into a dataframe/pandas
players1=pd.DataFrame(d_players1)

#to merge the datasets, the columns in the pandas dataframe have to be the same
players=pd.concat([players,players1])
print(players)

players=players.drop(['Unnamed: 0'],axis=1)
players=players.drop(['unnamed'],axis=1)
print(players)

#refresh the index values
players.players.reset_index()

#setting the index (and remove the default index)
players=players.set_index('PlayerID')
print(players)

#drop rows from a panda
len(players[players.Average<15])
ndx=players[players.Average<15].index
players=players.drop(ndx,axis=0)
len(players)
