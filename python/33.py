#!/usr/bin/python

# i ab ab
# j bc ca

for j in range(12,100):
 for i in range(11,j):
  if (((i%10==int(j/10))and(i*(j%10)==int(i/10)*j))or((int(i/10)==j%10)and(i*int(j/10)==j*(i%10))))and(i!=j):
   print i,j
#   print "(",i%10,"=",int(j/10),"and",i/j,"=",int(i/10)/j%10,") or (",int(i/10),"=",j%10,i/j,"=",i%10/int(j/10),")"
