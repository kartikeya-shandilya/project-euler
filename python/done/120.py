#!/usr/bin/python

sum=0
for a in range(3,1001):
 max=0
 for j in range(1,a):
  n1=int((j*a*a-1)/(2*a))
  n2=n1-1
  if n1%2==0:
   n=n2
  else:
   n=n1
  rem=(2*n*a)%(a*a)
  if rem>max:
   max=rem
 print a,n,max
 sum=sum+max

print "sum :",sum
