
import math

def contFrac(n):
    f=int(math.floor(n))
    d=n-f
    return f,1.0/d

cnt=0
lim=1000
for i in xrange(1,lim+1):
    x=math.sqrt(i)
    a=int(math.floor(x))
    ln=0
    if x!=a:
        n=1.0/(x-a)
        seq=[]
        while 1:
            f,n=contFrac(n)
            ln+=1
            if f==2*a:  break
    cnt+=ln%2

print "ans", cnt
