# -*- coding: utf-8 -*-
# ch6. Sets

s1=set(['V','I','G','Y','O','R'])
s2=set(['Q','W','E','R','I','P'])
print(s1)
type(s1)

#operations on a set
#union
s1.union(s2)
#intersection
s1.intersection(s2)
#difference
#A-B
s1.difference(s2)
#B-A
s2.difference(s1)

#symmetric difference= union - intersection
s1.symmetric_difference(s2)

#making a list unique
lov=['list','house','list','cat','random','value','house','zoo','random']

lov.sort()
print(lov)
#convert the list into a set
lov=list(set(lov))
print(lov)

















