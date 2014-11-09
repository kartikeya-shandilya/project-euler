#!/usr/bin/python

"""
def checkprime(j):
 from math import sqrt
 if j%2==0:
  return(0)
 for k in range(3,int(sqrt(j)+1)):
  if j%k==0:
   return(0)
 return(1)
"""

count=1
for a in range(3,1000000):
 val=1
 from math import sqrt
 if a%2==0:
  val=0
 for k in range(3,int(sqrt(a)+1)):
  if a%k==0:
   val=0
 count+=val
 rem=0
 if val==1 and count%2!=0:
  rem=(2*count*a)%(a*a)
 if rem>10000000000:
  print a,count,rem
  break
