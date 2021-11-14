# -*- coding: utf-8 -*-
#ch8: Functions

def triType(deg):
	if(deg == 0):
		msg="Invalid degree specified"
	else:
		if((deg>0) & (deg<90)):
			msg="Acute angled triangle"
		elif(deg==90):
			msg="Right angles triangle"
		elif((deg>90) & (deg<180)):
			msg="Obtuse angles trianlge"
		else:
			msg="Invalid"
	#return(msg)
	#can also return multiple values
	return(deg,msg)
	
degrees=71
d,rett=triType(degrees)
print("degree = {}, type = {}".format(d,rett))


#assignment: write a function to calc the factoraial of a number
def fact(num):
	facts=1
	if(num>=0):
		for i in range(1,num+1):
			facts=i*facts
	else:
		facts="invalid"
	return(facts)
	
fact(5)
fact(-1)
fact(4)
fact(0)
fact(1)


#mandatory vs optional prameters
def greetings(name=None):
	if(name is None):
		msg="hello anonymous user"
	else:
		msg="hello "+name
	return(msg)

greetings()
greetings("abc")

#assignment
#create a function to add a new element to dictionary at particular location
#parameters: dict, new key, new value, location
emp_data={}
def dicts(data,newkey,newval,newloc):
	data[newkey]=newval



dicts(emp_data,'name','abc',10)	
print(emp_data)


#if(loc<=len(data)):
#	for i in len(data):
#		data[i+1]=data[i]
#		i-=1


	




