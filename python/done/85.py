#!/usr/bin/python

min=1000
for i in range(1,3000):
 ii=i*(i+1)
 from math import sqrt
 j=int((sqrt(4*8000000/ii+1)-1)/2)
 jj=j*(j+1)
 kk=(j+1)*(j+2)

 diff=8000000-(ii*jj)
 if diff<0:
  diff=-1*diff
 digg=8000000-(ii*kk)
 if digg<0:
  digg=-1*digg

 dikk=diff
 if diff>digg:
  dikk=digg

 if dikk<min:
  min=dikk
  a=i
  b=j

print min,a,b 
