#!/usr/bin/python

cnt=0
for i in range(1,10000):
 tag=0
 num=i
 for j in range(1,51):
  num=num+int(str(num)[::-1])
#  print i,j,num,str(num/1)[::-1]
  if num==int(str(num)[::-1]):
   tag=1
   break
 if tag==0:
  print i
  cnt=cnt+1

print "count =",cnt
