# -*- coding: utf-8 -*-
#ch 10: Numpy ie Number Python

import numpy as np
list1=[1,3,5,8,10]
list2=[2,4,6,7,3]
type(list1)

#add two elemetns of 2 lists
list1+list2 #gives concatenation

#create a numpy array
arr1=np.array([1,3,5,8,10])
arr2=np.array([2,4,6,7,3])
type(arr1)

#returns the element-wise addition
arr1+arr2 

#download Numpy documentation from numpy.org for reference when needed

#number generation from 0 to N-1
num1=np.arange(20)

#convert the array to a 4x5 matrix
num1.reshape(4,5)

#fix the number of coloumns as rows dimensions are variable
num1.reshape(-1,5)



#generate 500 numbers
num2=np.arange(500)
#fix the number of coloumns as rows dimensions are variable
num2.reshape(-1,5)


#generate 350 numbers
num3=np.arange(350)
#fix the number of rows
num3.reshape(35,-1)


#shape and size
num1=num1.reshape(4,5)
num1.shape #rows, cols
num1.size #total no of elements

#change the array num1 to a 2x10 matrix
num1=num1.reshape(-1,10)
num1.shape #rows, cols


#shuffling the number set
num1=np.arange(30)
np.random.shuffle(num1)
num1

#convert it into a 6x5 matrix
num1=num1.reshape(-1,5)
print(num1)

#transpose a matrix
print(num1)
np.transpose(num1)

#queries
num1[num1>15]

#retrieve all numbers from teh matrix that are multiples of 3
num1[num1%3 == 0]

#generate a aequence between two numbers
np.linspace(0,1,10) # 10 numbers between 0 and 1
#round these numbers off
np.round(np.linspace(0,1,10),3)

#integer number generation
#-------------------------------

#method 1
rn1=np.random.randint(1,50,10) #10 random numbers between 1 and 50 with replacement
rn1
#ascending sort
np.sort(rn1)
#descending sort
-1*np.sort(-rn1)

#method 2
nums=np.arange(300)
np.random.choice(nums,20,replace=True)

#assignment: from the rn1 series, pick the the top 5 values
-1*np.sort(-rn1)[0:5]

#without replacement
#unique numbers
nums1=np.arange(30)
rn3=np.random.choice(nums1,20,replace=True)
print(np.sort(rn3))
rn3=np.unique(rn3)
print(rn3)

#float numbers
np.random.ranf(10) #10 random float numbers between 0 and 1

#10 random numbers in a given range
rf2=np.round(np.random.uniform(7,50,10),2)
print(rf2)

#add a number eg 5 to every element
rf2+5


#pre defined numpy arrays
#create a matrix and initialize it with 0
np.zeros((2,3)) #returns float
npa1=np.zeros((2,3),np.int32)
npa2=np.ones((5,6),np.int32)

#accessing a numpy array
npa1[0,0]=33.56
print(npa1)

npa1[1,] #2nd row all cols
npa1[:,2] #3rd col and all rows

#operations on an array
arr1=np.arange(1,7)
arr1
arr2=np.arange(4,10)
arr2

#concatenation of two numpy arrays
#1) traditional method
arr3=np.concatenate([arr1,arr2])
print(arr3)

#2) horizontal stacking
np.hstack([arr1,arr2])

#3) vertical stacking
np.vstack([arr1,arr2])

#repeating values
np.repeat(arr1,2) #repeat the values
np.tile(arr1,2) #repeat the seqence

#intersection
np.intersect1d(arr1,arr2)

#difference
#A-B
np.setdiff1d(arr1,arr2)

#B-A
np.setdiff1d(arr2,arr1)

#converting other datatypes into a numpy array
#converting a python list to a numpy array
lov1=[1,2,3,4,5,6]
lov1=np.asarray(lov1)

#swapping cols in numpy array
print(rn1)
rn1=rn1.reshape(-1,5)
rn1[:,[3,1,2,0]]


#statistical operation on an n dimentional arrays
arr10=np.random.randint(10,101,50).reshape(-1,5)
print(arr10)

#1)on entire matrix
np.max(arr10)
np.min(arr10)
np.sum(arr10)
np.mean(arr10)
np.std(arr10)
np.median(arr10)
np.percentile(arr10,25)

#2)on each row
np.max(arr10,axis=1)
np.min(arr10,axis=1)
np.sum(arr10,axis=1)
np.mean(arr10,axis=1)
np.std(arr10,axis=1)
np.median(arr10,axis=1)
np.percentile(arr10,25,axis=1)

#2)on each col
np.max(arr10,axis=0)
np.min(arr10,axis=0)
np.sum(arr10,axis=0)
np.mean(arr10,axis=0)
np.std(arr10,axis=0)
np.median(arr10,axis=0)
np.percentile(arr10,25,axis=0)


#numpy arithmetic
arr1+arr2
arr1-arr2
arr1/arr2
arr1*arr2

#returns the index of the value matchin gthe condition
np.where(arr1>5) #returns the index
arr1[np.where(arr1>5)] #returns the value

arr1[np.where((arr1>2)&(arr1<6))]

lst1=range(1000)
%timeit [i**2 for i in lst1]

lst2=np.arange(1000)
%timeit lst2**2



import scipy as sp
from scipy import fftpack as fft
from scipy import signal as sig
from scipy import linalg as lg
from scipy import integrate
dir(fft)
dir(sig)
dir(lg)
dir(integrate)
seq1=(1,2,3,4)
seq2=(5,6,7,8)
sp.convolve(seq1,seq2)

























































