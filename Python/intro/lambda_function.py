# -*- coding: utf-8 -*-
#Ch9: Lambda Functions
#also called pseudo functions

#standard way to create a function
def multip(x,y):
	return(x*y)
#to create a lambda function
multipl=lambda x,y : x*y
multipl(10,20)

add1=lambda a,b,c : a+b+c
add1(4,5,6)
add1(-5,10,30)

#to find smaller of two numbers
smlr=lambda x,y: x if x<y else y
smlr(5,6)

#to find larger of two numbers
lar=lambda x,y: x if x>y else y
lar(5,6)

#to double every value from a list
num=[1,2.2,3,5.6,8.4,10]
print(list(map(lambda x:x*2,num)))

import math
#area of a circle
area=lambda x:round(math.pi*x*x,2)
area(5)

#filter out values matching a specific conditions
nums=[1,2,3,4,5,6]
print(list(filter(lambda x:x>3,nums)))

#taking square root of numbers
lon=[12,4,9,36,16,64]
list(map(lambda x:round(math.sqrt(x),2),lon))

#print nums grater than 50
nums=[12,4,9,36,16,64,32,65,12,86,56,87,98]
print(list(filter(lambda x:x>50,nums)))

#write a function to check the input is a palindrome or not
#import string
p='madam'
def reverse(str1):
	flag=0	
	for i in range(0,len(str1)):
		if(str1[i]!=str1[len(str1)-i]):
			flag=1
	if(flag==0):return('Palindrome')
	else:return('Not a palindrome')

ans=reverse(p)
print(ans)
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	