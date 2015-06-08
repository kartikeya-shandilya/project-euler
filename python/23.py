#!/usr/bin/python

abund=[0.9]
k=0

for n in range(5,21000):
 divsum=0
 from math import sqrt
 k=int(sqrt(n))+1
 from math import sqrt
 if sqrt(n)%1==0:
  from math import sqrt
  k=int(sqrt(n))
 for j in range(1,k):
  if n%j==0:
   divsum=divsum+j+int(n/j)
  j=j+1
 divsum=divsum-n
 if sqrt(n)%1==0:
  divsum=divsum+int(sqrt(n))
 if divsum>n:
#  print "abundant",n,divsum
  abund.append(n)
  k=k+1

print "k =",k

sum=0
for a in range(1,21000):
 tag=0
 for i in abund:
#  print "a, i,",a,i
  try:
   if abund.index(a-i):
    tag=1
    print a,"=",i,"+",a-i
    break
  except ValueError:
   continue
  if i>a:
   break
# print "a, tag,",a,tag
 if tag==0:
  sum=sum+a
  print a

print "sum =",sum
#print abund

