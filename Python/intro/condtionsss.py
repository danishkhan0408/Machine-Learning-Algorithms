# -*- coding: utf-8 -*-
#ch 7: conditional statements/loops/operators

#IF
temp=35
if temp>=30 :
	print("Temperature= {}".format(temp))
	print("warm day")
else:
	print("cool day")	


#elseif ladder
if(temp==30):
	print("temp is 30")
elif(temp==32):
	print("temp is 32")
else:
	print("temp is 35")
	

#operators with if else
#AND
gpa=4.7
grade='A'
if((gpa>4) & (grade=='A')):
	print("distincton")
else:
	print("no disctinction")

#OR
gpa=4.7
grade='A'
if((gpa>5) | (grade=='A')):
	print("distincton")
else:
	print("no disctinction")

#NOT !
gpa=4.7
grade='A'
if(gpa!=4.7):
	print("distincton")
else:
	print("no disctinction")


#assignment 1
	#write a nested if for the following
	#performance score=<1-100>
	#print the performance score using the following conditions
	#perf score 	performance
	#90-100 	 	outstanding
	#80-89 	 	    very good
	#70-79 	 	    good
	#rest 	        needs improvement
	
perf=100

#method1
if(perf<70):
	print("needs improvement")
elif((perf>=70)&(perf<=79)):
	print("good")
elif((perf>=80)&(perf<=89)):
	print("very good")
else:
	print("outstanding")

#method2
if(perf in range(0,101)):
	if(perf in range(0,70)):
		print("needs improvement")
	elif(perf in range(70,80)):
		print("good")
	elif(perf in range(80,90)):
		print("very good")
	else:
		print("outstanding")
else: 
	print("invalid score")


#for loop
lov=['computer','mouse','blackboard','data','cat','rain']

#1. using the index
for i in range(0,len(lov)):
	print(lov[i])
	
#2. using the value
for e in lov:
	print(e)

#assignment 2
#for every word in the list 
#cuount the number of vovels in it
lov=['computer','mouse','blackboard','data','cat','rain']
vow=['a','e','i','o','u']
#method 1
for i in lov: #selecting each word from lov
	count=0
	for e in i: #selecting the individual character from each word in lov
		for j in range(0,len(vow)): #for comparing with vowels
			if(e==vow[j]):
				count=count + 1
	print(str(i)+" "+str(count))

#method 2
for k in lov:
	counter=k.count('a')+k.count('e')+k.count('i')+k.count('o')+k.count('u')
	print(str(k)+" "+str(counter))


#'None' value
#not a space,or a null,or 0 or a blank
total=None
str(total)
if(total is None):
	print("None value")
else: 
	print("Not a None")


#while loop
i=10
while(i>3):
	print('the value of i ='+str(i))
	i-=1





































