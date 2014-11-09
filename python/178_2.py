
def popRange(i,j,tRange):
    for elm in oReach[i]:
        l=min(elm[0],j); u=max(elm[1],j)
        try:    tRange[(l,u)]+=oReach[i][elm]
        except: tRange[(l,u)] =oReach[i][elm]
    return tRange

def mrgRange(p,q):
    for elm in q:
        try:    p[elm]+=q[elm]
        except: p[elm] =q[elm]
    return p

def newReach():
    nuReach=[{} for i in xrange(10)]
    for i in xrange(10):
        if i>0: nuReach[i-1]=mrgRange(nuReach[i-1],popRange(i,i-1,{}))
        if i<9: nuReach[i+1]=mrgRange(nuReach[i+1],popRange(i,i+1,{}))
    return nuReach

def pandigital(n,sm):
    for i in xrange(10):
        if (0,9) in n[i]: sm+=n[i][(0,9)]
    return sm   

ans=0; oReach=[]; mx=40;
for i in xrange(1,10):
    oReach=[{} for j in xrange(10)]
    oReach[i][(i,i)]=1
    for j in xrange(2,mx+1):
        nReach=newReach()
        oReach=nReach
        ans+=pandigital(nReach,0)
    print i,pandigital(nReach,0),ans
