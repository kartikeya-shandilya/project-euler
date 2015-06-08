#!/usr/bin/python

p=0
q=0
r=0
s=0

for a in range(10,200000):
 n=a
 uniqlist=[]
 while n>1:
  from math import sqrt
  for j in range(2,2+int(sqrt(n))):
   if n%j==0:
    n=n/j
    try:
     if uniqlist.index(j):
      n=n
    except:
     uniqlist.append(j)
    j=n+2
    break
  if j!=int(n+2):
   try:
     if uniqlist.index(n):
      n=n
   except:
    uniqlist.append(n)
   break
 p=len(uniqlist)
 if (a%10000==0):
   print "for",a,uniqlist
   print p,q,r,s
 if p==4 and q==4 and r==4 and s==4:
  print "Surprise",a,uniqlist;
 s=r
 r=q
 q=p

