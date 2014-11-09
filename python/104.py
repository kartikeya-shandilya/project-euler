#!/usr/bin/python

nine=[1,2,3,4,5,6,7,8,9]

a=1
b=1
for i in range(3,1000000):
 b=a+b
 a=b-a
 c=str(b)
 first=[]
 last=[]
 if len(c)>9:
  for j in range (1,10):
   first.append(int(c[j-1]))
   last.append(int(c[len(c)-j]))
 first.sort()
 last.sort()
 if i%1000==0:
  print i
 if last==nine and first==nine:
  print i

