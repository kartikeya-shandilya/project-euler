#!/usr/bin/python

total=0
for i in range(1,10000):
 sum1=0
 for j in range(1,i):
  if i%j==0:
   sum1=sum1+j
 sum2=0
# print "a:",i,sum1
 if sum1>1:
  for j in range(1,sum1):
   if sum1%j==0:
    sum2=sum2+j
 if (i==sum2)and(i!=sum1):
  print "match:",i,sum1
  total=total+i

print total
