#!/usr/bin/python

def checkprime(j):
 from math import sqrt
 if j%2==0:
  return(0)
 for k in range(3,int(sqrt(j)+1)):
  if j%k==0:
   return(0)
 return(1)

count=0
for i in range(1,600):
 n=3*i*i+3*i+1
 if n<1000000 and checkprime(n)==1:
  count += 1

print count
