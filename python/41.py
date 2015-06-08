#!/usr/bin/python

def checkprime(j):
 if j%2==0:
  return(0)
 from math import sqrt
 for k in range(3,int(sqrt(j))+1):
  if j%k==0:
   return(0)
  k=k+1
 return(1)

def permutate(seq):
 if not seq:
  return [seq] # is an empty sequence
 else:
  temp = []
  for k in range(len(seq)):
   part = seq[:k] + seq[k+1:]
   for m in permutate(part):
    temp.append(seq[k:k+1] + m)
  return temp

#list=[]
list=permutate('1234567')
list.sort()
print len(list)

for i in range(1,1000):
 k=list[len(list)-i]
 if checkprime(int(k)):
  print k
  break
