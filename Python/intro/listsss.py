# -*- coding: utf-8 -*-

#ch3 LISTS
#lists are represented by [ ]
#index tsrats from 0
#supports mutation


#clear and empty list
mylist=[]
type(mylist)

#create a list with values
months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov',' dec']
print(months)

#total no of elements in the list
len(months)

#accessing the list
#use the index
months[0]

months[-1]

#skip parameter
#start at the first element of list
#end at last element of list
#skip 5
m5=months[::5]
print(m5)

#Assignment 1 create 2 lists odd momths and even months

even_months=months[::2]
odd_months=months[1::2]

print(even_months)
print(odd_months)

#List operations
#adding new element to a list
months.append('M1')
months.append('M2')
months.append('M3')

print(months)

#add an element anywhere in the list
months.insert(0,"M0") #1st position
print(months) 

#add a new value in the location "Sep"
ndx=months.index("sept")
months.insert(ndx,"M9")
print(months) 


#change the existing element's value
months[0]="Month-0"
print(months) 

#for replacing all the months with an index
for i in range(len(months)):
	text="Month {}".format(i)
	months[i]=text
print(months) 

#remove elements from a list
del months[0]
print(months)
months.pop(months.index('Month 1')) 
print(months) 

#deep copy = pass by value
#shallow copy = pass by reference

#copy a list by pass by refernce and pass by value

#copy1 = shallow copy
copy1=months

del copy1[copy1.index('Month 5')]
del copy1[copy1.index('Month 6')]

print(copy1)
print(months)

#copy 2 = deep copy
copy2=months.copy()
del copy2[copy2.index('Month 2')]
del copy2[copy2.index('Month 3')]

print(copy2)
print(months)

#list of numbers
num_lists=list(range(1,51))
print(num_lists)

#stats on lists
max(num_lists)
min(num_lists)
sum(num_lists)

meann=sum(num_lists)/len(num_lists)
print(meann)

num_list2=list(range(51,101))

#concatenation of lists
num_list3=num_list2+num_lists

#breaks in range
list(range(1,51,5))


for i in range(len(num_lists)):
	print( num_lists[i] + num_list2[i] )



#nested lists

table= [list(range(1,21,2)),
			list(range(1,21,5)),
			list(range(1,21,9))]
print(table)

#accessing the nested list
#entire first element list
table[0]
#first 5 of first element
table[0][0:5]

#fetch the 3rd element from the 2nd element
table[1][2]

#nested list for strings
country=['india','us','uk','china']
capital=['delhi','washington','london','beijing']
currency=['rupee','dollar','pound','yuan']

maps=[country,capital,currency]

print(maps)

maps[0]
maps[0][0]
maps[0][0][0:3]

#assignment
for i in range(3):
	print(maps[i],maps[i+1][i])


#assignmet create two lists of 10 numbers each, having 1,2 and 3 digit numbers
#multiply each 1 digit number of 1st list with all the 1 digit numbers of the 2nd list
#multiply each 2 digit number of 1st list with all the 2 digit numbers of the 2nd list
#random integers without replacement
import random as r
l11 = r.sample(range(1,9),3)
l12 = r.sample(range(10,99),3)
l13 = r.sample(range(100,999),4)
list1=l11+l12+l13

l21 = r.sample(range(1,9),3)
l22 = r.sample(range(10,99),3)
l23 = r.sample(range(100,999),4)
list2=l21+l22+l23

print(list1)
print(list2)

for i in range(0,len(list1)):
	for j in range(0,len(list2)):
		if((len(str(list1[i]))==len(str(list1[j])))):
			mul1=list1[i]*list2[j]
			print(str(list1[i])+" * "+str(list2[j])+" = "+str(mul1))



















