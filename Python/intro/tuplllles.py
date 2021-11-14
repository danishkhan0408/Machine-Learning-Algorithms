# -*- coding: utf-8 -*-
#ch 4 Tuple

#similar to lists but represented by () and is non mutable ie nomodifications can be performed on it except addition of new elements
#lists have homogenous data while tuple has heterogenous data

#empty tuple
tup=()
type(tup)

#create a tuple with some values
tup=('english','accounts','physics','chemistry','hindi','science')

print(tup)

#total no of element sin a tuple
len(tup)
#accessing a tuple
#index starts from Zero
tup[0]

#first 3 elements
tup[0:3]

#concatenate tuples
t2=('stats','hindi','accounts')
tup=tup+t2

print(tup)

#try to change a tuple's element
tup[0]="Grammar"


#to change the contents of a tuple
#1) convert the tuple to a list
tup=list(tup)
print(tup)

#2)make the required changes
tup[0]="grammar"
del tup[len(tup)-1]
print(tup)

#3)convert it back into a tuple
tup=tuple(tup)
print(tup)

#packing and unpacking a tuple

#packing a record
rec1=('sriram',True,45,172.4,1)

#unpack a record
(name,active,age,height,gender)=rec1
print(name)
print(active)
print(age)
print(height)
print(gender)

#joining words from a tuple ot forma a sentace/recod
t3=('mary', 'had','little','lamb')
' '.join(t3)
#create a csv
','.join(t3)


#check for exisistence of a word in a tuple
'hindi' in tup
'python' in tup


#nested tuple
temp_=(
	   ('e1',100,'13-09-2019',20),
	   ('e2',101,'01-01-2019',32),
	   ('e3',102,'03-05-2019',12)
	 )

temp_[0]

#assignment
#empname,empid,joindate,exp
#store the values from the tuple into these lists

#creat an empty list
empname=[]
empid=[]
joindate=[]
exp=[]

for i in range(len(temp_)):
	
	(v1,v2,v3,v4)=temp_[i]
	empname.append(v1)
	empid.append(v2)
	joindate.append(v3)
	exp.append(v4)

print(empname)
print(empid)
print(joindate)
print(exp)


#assignment 2
#create a tuple of grocery shopping items (10 rows(items))
#cols:
# itemname    qty    price   total_price
#__________    ___    _____   ___________

#1 total_price=qty*price
#2 calc the grand total 
#3 identify teh costliest adn the cheapeast item


bill=(
	   ('item1',10,130,0),
	   ('item2',12,30,0),
	   ('item3',4,1300,0),
	   ('item4',42,10,0),
	   ('item5',12,15,0),
	   ('item6',8,112,0),
	   ('item7',76,18,0),
	   ('item8',34,92,0),
	   ('item9',16,71,0),
	   ('item10',12,130,0)
	 )


itemname=[]
qty=[]
price=[]
total_price=[]

for i in range(len(bill)):	
	(i1,i2,i3,i4)=bill[i]
	itemname.append(i1)
	qty.append(i2)
	price.append(i3)
	total_price.append(i4)

len(total_price)
for j in range(len(total_price)):
	total_price[j]=qty[j]*price[j]
	
print(itemname)
print(qty)
print(price)
print(total_price)
bill=tuple(bill)
print(bill)









































