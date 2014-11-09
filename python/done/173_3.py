#!/usr/bin/python

count=0
for i in range(3,27):
 for j in range(1,i-1):
  if (i%2==j%2)and(i*i-j*j<=100):
    count+=1
    print i,j,"-",count

print "final =",count
