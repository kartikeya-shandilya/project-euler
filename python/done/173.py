#!/usr/bin/python

count=0
for i in range(3,26):
 if i<12:
  count += int((i-1)/2)
 else:
  from math import sqrt
  count += int(i-1-int(sqrt(i*i-100)))/2
 if i%1==0: 
  print i,"-",count

print "final =",count
