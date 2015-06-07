
from math import floor, log, sqrt

def getFrac(k):
  num = log((1+sqrt(1+4*k))/2.0)//log(2)
  den = (1+sqrt(1+4*k))//2-1.0
  return num / den

check = 1/12345.0

def search(l,r):
  print "searching...", l, r
  m = (l+r)//2
  y1 = getFrac(m)
  y0 = getFrac(m-1)
  if y1<check and y0>=check:
    print m
    return
  elif y1>=check:
    search(m,r)
  else:
    search(l,m)

search(10,10**11)

