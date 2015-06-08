#!/usr/bin/python

#a=90
#b=99
max=0

for a in range (1,100):
 for b in range (1,100):
  c=str(a**b)
  sum=0
  for i in range (0,len(c)):
   sum=sum+int(c[i])
  #print a,b,c,sum
  if sum>max:
   max=sum
   p=a
   q=b
   r=c

print "ans:"
print p,q,r,max
