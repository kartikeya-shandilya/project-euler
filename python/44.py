#!/usr/bin/python

for i in range(1,2500):
 for j in range(1,2500):
  x=i*(3*i-1)/2
  y=j*(3*j-1)/2
  from math import sqrt
  if (sqrt(24*(x+y)+1)+1)%6==0 and (sqrt(24*(abs(x-y))+1)+1)%6==0:
    print i,j,x,y,x+y,x-y
