#!/usr/bin/python

count=0
prev=0
for n in xrange(1,10000):
 k=n
# if n%100000==0:
#  print n
 div=[]
 from math import sqrt
 while k!=1:
  for j in range(2,k+1):
   if k%j==0:
    div.append(j);
    k=int(k/j)
    break
   if j>2:
    j=j+1
 val=1
 div.sort()
 past=0
 for i in range(0,len(div)):
  if past!=0:
   if past==int(div[i]):
    curr=curr+1
    if i==len(div)-1:
     val=val*(curr+1)
   else: 
    if past!=int(div[i]):
     val=val*(curr+1)
     curr=1
     if i==len(div)-1:
      val=val*(curr+1)
  else:
   curr=1
  past=int(div[i])
# print n,div,val
 if val==prev:
  count=count+1
 prev=val

print "count =",count
