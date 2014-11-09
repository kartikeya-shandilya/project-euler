#!/usr/bin/python

x=1
for i in range(1,100):
 x=x*i

print x

sum=0
while x>0:
 sum=sum+x%10
 x=int(x/10)

print sum
