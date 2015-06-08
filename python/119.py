#!/usr/bin/python

arr=[]
for i in range(3,10):
 arr.append(int(614656**(1/(1.0*i))))

print arr
i=3
for j in arr:
 k=0
# print "start",i,j
 while k<5000000000000000:
  k=j**i
  l=0
  for m in range(0,len(str(k))):
   l=l+int(str(k)[m])
  if l==j:
   print "YES",i,j,k,l
  j+=1
# print "stop",i,j,k,l
 i+=1

