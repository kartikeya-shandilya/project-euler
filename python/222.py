
from math import sqrt

def addBall(r,s):
    return s+sqrt(2*r*s-r*r)


l=100; a=50; r=100;
i=0; ct=1;
while 1:
    if ct%2==1: b=30+i
    else:       b=50-i
    l+=addBall(r,a+b)-2*a
    print a, b, l, i, ct
    if ct%2==1: i+=1
    ct+=1
    a=b
    if ct==21:  break

print l
print ""

l=100; a=50; r=100;
i=1;
while 1:
    b=50-i
    l+=addBall(r,a+b)-2*a
    print a, b, l, i, ct
    i+=1
    a=b
    if a==30:  break

