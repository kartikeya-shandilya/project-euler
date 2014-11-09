#!/usr/bin/python

count=0
for i in range(3,250002):
 if i<1001:
  for j in range(1,i-1):
   if i%2==j%2:
    count+=1
#    print "i =",i,"j =",":",j,count,(i*i-j*j)
 else:
  from math import sqrt
  k=sqrt(i*i-1000000)
  if k%1!=0: 
   k=int(k)+1
  else:
   k=int(k)
  for j in range(k,i-1):
   if i%2==j%2:
    count+=1
#    print "i =",i,"j =",":",j,count,(i*i-j*j)
# if i%1==0: 
#  print i,"-",count

print "final =",count
