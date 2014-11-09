
from math import sqrt, ceil

rep = [ ]
com = [1]
tot = 1
n   = 2
lim = 10**12

while 1:
  p = 1
  s = 1+n**p
  while s < lim:
    if s in rep:
      if s not in com:
        com.append(s)
        tot += s
    elif p!=1:
      rep.append(s)
    p += 1
    s += n**p
  if not n%100000: print n,p
  if p==2:
    print "n",n
    break
  n += 1

#print "rep",rep
#print "tot",tot
#print "com",com
#print "rest",[x for x in rep if (x>n+1 and x not in com)]
print "sum",tot + sum([x for x in rep if (x>n+1 and x not in com)])


