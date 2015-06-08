#/usr/bin/python

import math

a=0
b=1

m=0
n=1
while n>0:
 m=m+1
 n=a+b
 a=b
 b=n
 from math import log
 k=log(n)/log(10)
 if k>999:
  n=0

print m

