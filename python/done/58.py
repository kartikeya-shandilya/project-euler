#!/usr/bin/python

def checkprime(j):
 from math import sqrt
 if j%2==0:
  return(0)
 for k in range(3,int(sqrt(j)+1)):
  if j%k==0:
   return(0)
 return(1)

tot=1
pri=0
k=1
for i in range(0,100000):
 for j in range(1,5):
  k=k+2*(i+1)
# print k
  tot+=1
  pri+=checkprime(k)
# print i,pri,tot,(pri/(1.0*tot))
 if (pri/(1.0*tot)<0.1):
  print 2*i+3
  break
