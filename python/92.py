#!/usr/bin/python

cnt=0
for i in range(1,10):
 print i,":",
 while (i!=1 and i!=89):
  print i,"-",
  l=0
  x=str(i)
  for j in range(0,len(x)):
   l=l+int(x[j])**2
  i=l
 print i
 if i==89:
  cnt=cnt+1

print "count :",cnt
