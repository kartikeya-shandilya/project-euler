#!/usr/bin/python

a=1000
while a>0:
 n=a*(a+1)/2
 div=0
 from math import sqrt
 for j in range(1,int(sqrt(n))):
  if n%j==0:
   div=div+1
#print a,n,div
 if div>=250:
  a=-a
 else:
  a=a+1

print -a
