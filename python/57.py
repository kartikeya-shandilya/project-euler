#!/usr/bin/python

a=1
b=1
c=0
for i in range (1,1000):
 a=a+2*b
 b=a-b
 print i,a,b
 if (len(str(a))>len(str(b))):
  c+=1

print "ans:",c
