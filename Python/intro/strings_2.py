# -*- coding: utf-8 -*-
#2. Strings

str1= 'c';type(str1)
str2= "c";type(str2)
str3= 'word';type(str3)
str4= "word";type(str4)

str5="machine learning is the best"
type(str5)
#length including the spaces
len(str5)

#accessing the string vector
str5[0]
str5[0:5]

#to access the last character
str5[-1]
str5[len(str5)-1]

#string concatenation
str5[0:5]+str5[9:13]

#find string within a string

str6="this place is haunted, the place has been like this for a long time. no one visits this place, the place is dark and spooky"
word="place"
str6.find(word) #first occourance
#last occourance
str6.rfind(word)

#check if a sentence begins with a word
str6.startswith(word)

#number of occourance of the word
str6.count(word)

#alternate method to count no of occourance of the word
count=0
for i in len(str6):
    tot=0
    for j in len(word):
        if(str6[i]==word[j]):
            tot= tot+1
    if( tot == len(word)):
        count= count + 1
    
print("count = "+str(count))


#check existence of a word in a given string
#returs true/false
word in str6
'mouse' in str6

#find and replce a string
str6.replace(word,'site') #only displays the replaced statement doesnt save it
#str6=str6.replace(word,'site')


#string libraries
import string as s

#remove different types of spaces from string - split/join method
word="    python  "
word.lstrip() #left strip
word.rstrip() #right strip
word.strip() #remove all spaces


#removeing special white spaces like Tabs,<ctrl return or enter>

sent4="     this movie is bad, the action was poor      and the sogs were   not related             to the story \n \n \n could have             better"

sent4.strip() #will not be of much use
#two step process
words=sent4.split()
sent5=' '.join(words)

#ssplit at special characters
str5="sriramn$25$training$pune$M"

#split the sentence into individual column values
str5.split("$")

#standard library
s.ascii_uppercase
s.ascii_lowercase

#replicating a word n times
str6='company ' *5
print(str6)
str6[0:5]

#use either \\ or / for setting file path

#assignment: Create a list of values and print each element by replacing the plus sign with a single space

#import string
texts=['computer+program','new+delhi','artificial+intelligence','seas+facing','bungalow+society','software+engineer','highspeed+internet','slow+coach','high+density','clear+weather']

for j in texts:
	print(' '.join(j.split('+')))