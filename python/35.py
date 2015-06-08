#!/usr/bin/python

def checkprime(j):
 from math import sqrt
 if j%2==0:
  return(0)
 for k in range(3,int(sqrt(j)+1)):
  if j%k==0:
   return(0)
 return(1)

count=4

for i in range(11,1000000):
 perm=[]
 perm.append(i)
 s=str(i)
 for t in range(0,len(s)):
  u=str(perm[t])
  w=u[-1]
  for v in range(0,len(u)-1):
   w += u[v]
  perm.append(w)
 if (t!=0)and(perm[0]==perm[-1]):
  break
# else:
#  print "perm =",perm[0],perm[1],perm[2],perm[3]
 tag=len(s)
 for x in range(0,len(s)):
  tag-=checkprime(int(perm[x]))
 if tag==0:
  print i
  count+=1

print "count =",count
