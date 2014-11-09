#!/usr/bin/python

sq=[]
for i in range(0,10):
 sq.append(i*i)

tot=0
for i in range(1,1000000):
 j=str(i)
 sum=0
 for k in range(0,len(j)):
  sum=sum+sq[int(j[k])]
 from math import sqrt
 if sqrt(sum)%1==0:
  print i,sum
  tot=tot+sum

print "final =",tot
