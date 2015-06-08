#!/usr/bin/python

import math

def checkprime(j):
 if j%2==0:
  return(0)
 for k in range(3,int(sqrt(j))+1):
  if j%k==0:
   return(0)
  k=k+1
 return(1)

def check(j):
 if j%2==0:
  return(0)
 from math import sqrt
 for k in range(3,int(sqrt(j))+1):
  if j%k==0:
   return(0)
  k=k+1
 return(1)

#print check(33271)

prime=[]
prime.append('2')

k=0
for i in range(3,10000):
 ptag=1
 for j in range(0,len(prime)):
  from math import sqrt
  if (i%int(prime[j])==0):
   ptag=0
   break
  if int(prime[j])>int(sqrt(i)):
   break
 if ptag==1:
  prime.append(str(i))
  k=k+1

prime.pop(0)
print k

"""
a=3
b=7
if checkprime(int(str(a)+str(b)))==1 and checkprime(int(str(b)+str(a)))==1:
 print "ok"

print prime[1]%5
print prime[2]%5

print checkprime(int(str(2)+str(3)))
print checkprime(int(str(3)+str(2)))

for i in range(0,k+1):
 if i%100==0:
  print i,prime[i]
"""

"""
for a in range(0,2500):
 m=prime[a]
 for b in range(a-1,2500):
  n=prime[b]
#  print a,b
  if checkprime(int(str(m)+str(n)))==1 and checkprime(int(str(n)+str(m)))==1:
   for c in range(b-1,2500):
    o=prime[c]
    if checkprime(int(str(m)+str(o)))==1 and checkprime(int(str(n)+str(o)))==1:
     if checkprime(int(str(o)+str(m)))==1 and checkprime(int(str(o)+str(n)))==1:
#      print a,b,c
      for d in range(c-1,2500):
       p=prime[d]
       if m+n+o+p>20000:
         break
       if checkprime(int(str(m)+str(p)))==1 and checkprime(int(str(n)+str(p)))==1 and checkprime(int(str(o)+str(p)))==1:
        if checkprime(int(str(p)+str(m)))==1 and checkprime(int(str(p)+str(n)))==1 and checkprime(int(str(p)+str(o)))==1:
         print m,n,o,p
         for e in range(d-1,2500):
          q=prime[e]
          if checkprime(int(str(m)+str(q)))==1 and checkprime(int(str(n)+str(q)))==1 and checkprime(int(str(o)+str(q)))==1 and checkprime(int(str(p)+str(q)))==1:
#           print "passed 1"
           if checkprime(int(str(q)+str(m)))==1 and checkprime(int(str(q)+str(n)))==1 and checkprime(int(str(q)+str(o)))==1 and checkprime(int(str(q)+str(p)))==1:
            print m,n,o,p,q,"done, sum:",m+n+o+p+q
#           else:
#            print "failed 2"
#          else:
#           print "failed 1"
"""

for i in prime:
 print i,":"
 for j in prime[prime.index(i):]:
  if check(int(i+j)) and check(int(j+i)):
   for k in prime[prime.index(j):]:
    if check(int(i+k)) and check(int(j+k)) and check(int(k+i)) and check(int(k+j)):
     for l in prime[prime.index(k):]:
      if check(int(i+l)) and check(int(j+l)) and check(int(k+l)) and check(int(l+i)) and check(int(l+j)) and check(int(l+k)):
#       print i,j,k,l
#       if int(i)+int(j)+int(k)+int(l)>25000:
#        break
       for m in prime[prime.index(l):]:
        if check(int(i+m)) and check(int(j+m)) and check(int(k+m)) and check(int(l+m)) and check(int(m+i)) and check(int(m+j)) and check(int(m+k)) and check(int(m+l)):
         print i,j,k,l,m,"sum:",int(i)+int(j)+int(k)+int(l)+int(m)

