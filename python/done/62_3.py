#!/usr/bin/python

list=[]
for i in range(1,10000):
 j=i**3
 l=[]
 for k in str(j):
  l.append(k)
 l.sort()
# z=['|']
# z.append(i)
# list.append(l+z)
 list.append(l)
# print list

list.sort()
for elm in list:
  print elm

