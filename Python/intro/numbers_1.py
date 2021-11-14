# -*- coding: utf-8 -*-
#1. variable and numbers

msg="my first program"
print(msg)

#to get the datatype
type(msg)

#coerce - to change data type
msg=100
type(msg)
 
#to import a library
import os
dir(os)
os.getcwd() #to get the current working directory

#numbers

#[] indicates a list
#1) range of numbers
list(range(1,10))

#1) first 20 numbers
list(range(1,21))

#number series from 0
list( range(5))

#numbers with intervals 1 to 20 skip 4
list(range(1,21,4))

#odd numbers b/w 1 and 30
odds=list(range(1,31,2))

#even numbers b/w 1 and 30
even=list(range(0,31,2))

print(even)
print(odds)

#generate random numbers
import random as r

# generate one random number
print(r.randint(1,10))

#use a for loop to generate n random numbers with replacement
for i in range(10):
    print("value of i = "+str(i))
    print(r.randint(1,11))

#random integers without replacement
uniq = r.sample(range(10,101),20)
uniq.sort()
print(uniq)

#random float numbers
rf=r.uniform(1,10)
print(rf)

#reduce the digits after the decimal point
rf=format(rf,'.2f')
print(rf)
type(rf)
rf=float(rf)
type(rf)



#generate 50 GPS'a between 1.0 and 5.0
for i in range(50):
    print("student "+str(i))
    gpa=float(format(r.uniform(1,5),'.2f'))
    print(gpa)


#arithmetic operations
#to calc the perimeter of a rectangle
import math
leng=12.56
bre=3.92
peri = 2*(leng + bre)
print("perimeter =" +str(peri))

modd= 10%3
print(modd)

x=pow(2,3)
print(x)

dir(math)

math.factorial(5)

#take user input
y=input("enter a number")
print(y)
type(y)



#calc the area of a circle
radius=float(input("enter a radius of the circle"))
area=math.pi*pow(radius,2)
print("area= "+str(area))


#calc the area of a cylinder
radius=float(input("enter a radius of the cylinder"))
height=float(input("enter a height of the cylinder"))
area = 2*math.pi*radius*height
print("area= "+str(area))


#assignment: take any random negative number, perform the following in one line of code in the igven sequence
#double, divide by pi, convert result to +ve number
x=r.randint(-999,-1)
print(x)
print(abs(round((2*x)/math.pi,2)))

#assignment 10 random integers that are divisible by 8
i=0
num=[]
while(i<10):
	y=r.randint(0,999)
	if(y%8==0):
		num.append(y)
		print(y)
		i+=1
print(num)
	














