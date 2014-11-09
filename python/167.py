#!/usr/bin/python

ulam = [1,2,3]

from time import time  
print time(),"\n"

for cand in range(4,1000):
#  print cand,ulam
  count=0
  for i in ulam:
   for j in ulam:
    if (i<j)and(i+j)==cand:
     count+=1
  if count==1:
    ulam.append(cand)

print ulam,"\n"

from time import time  
print time()  
