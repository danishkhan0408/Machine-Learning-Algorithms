# -*- coding: utf-8 -*-
#ch5 Dictionary
#represented wiht {}

#createa a blank dictionary
dict1={}
type(dict1)

#add key-value pairs to the dictionary
dict1['one']='sports'
dict1['two']='hindi'
dict1['three']='english'
dict1['four']='comedy'
dict1['five']='learning'
dict1['six']='music'
dict1['seven']='news'

print(dict1)

#keys are unique
dict1['seven']='cartoon'

#assingment
#create a dictionary in the foll format for the dorst twenty numbers
#key   value
#1 	   1
#2     2
#3     9


sq={}
for i in range(1,21):
	sq[i]=i*i

print(sq)



#access a dictionary
#1. with the key
dict1['one']
dict1['seven']
dict1.keys()
## to check for the keys
'1' in dict1.keys()
'one' in dict1.keys()

#2.items()
dict1.items()

for k,v in dict1.items():
	print("Key={},value={}".format(k,v))

#3.using values
dict1.values()

#dropping a key value from a dictionary
del dict1['seven']
dict1.keys()

#keys values cannot be changed
#create a new key and copy the value, then delete the one to be deleted

dict1['superone']=dict1['one']

del dict1['one']
dict1.keys()


#dictionary with key-multiple vals
#create a dataset with the following cols/vals

#playerId - seq(1:20)
#playerName - char(5)
#matches - numeric(1-300)
#runs - numeric(1-15000)
#avg - float(1.0 - 60.0)
#age - numeric(18-36)


#player id
playerId=list(range(1,21))
print(playerId)


#player name
#s.ascii_uppercase+s.ascii_lowercase



import random as r
import string as s
#matches
matches=()
for i in range(1,21):
    matches = r.sample(range(1,301),20)
print(matches)

#runs
runs=()
for i in range(1,21):
    runs = r.sample(range(1,15000),20)
print(runs)

#avg
avg=()
for i in range(1,21):
    avg = r.sample(range(0,60),20)    
print(avg)

#age
age=()
for i in range(1,21):
    age = r.sample(range(18,38),20)
print(age)

#name
s.ascii_letters
names = r.choices(s.ascii_lowercase,k=20) # where k is the number of names
print(names)


d_players={'PlayerID':playerId,
		   'Matches':matches,
		   'Runs':runs,
		   'Average':avg,
		   'Age':age}

print(d_players)
d_players['Age']

#first three player id's


























