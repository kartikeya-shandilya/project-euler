
from math import sqrt
from bisect import bisect_left

def getSize(node):
    a,b=node; c=a-b
    x=(c+sqrt(c**2+4))/2.0
    y=1.0/x
    d=sqrt((y-b)**2+(x-a)**2)
    return d/sqrt(2)

def getNodes(node):
    a,b=node; d=getSize(node)
    return [(a+d,b),(a,b+d)]

node=(1,0)
siz=0; cnt=0
nrank=[node]
drank=[getSize(node)]

while 1:
    siz+=1
    mxsiz=drank.pop(-1)
    mxNod=nrank.pop(-1)
    if abs(mxNod[0]-2.495943999834191)<0.000001:
        cnt+=1; print siz, mxsiz, mxNod
    for node in getNodes(mxNod):
        d=getSize(node)
        if d<0.00075: continue
        idx=bisect_left(drank,d)
        nrank.insert(idx,node)
        drank.insert(idx,d)
    if cnt==4: break
