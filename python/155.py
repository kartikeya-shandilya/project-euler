
def gcd(x,y):
    a=max(x,y)
    b=min(x,y)
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)


def simp(n,d):
    x=gcd(n,d)
    return (n/x, d/x)


initSets={1:set([(1,1)]), 2:set([(1,2),(2,1)])}

def capCircs(x):
#    print "x", x
    if x in initSets:
            return initSets[x]
    z=set([])
    for n in xrange(1,x+1):
        z=set([])
        for i in xrange(1,(n+1)/2):
            if i in initSets:
#                print "taken", i
                a=initSets[i]
            else:
#                print "calc", i				
                a=capCircs(i)
                initSets[i]=a
#                print "initSets", initSets
            if n-i in initSets:	
#                print "taken", n-i
                b=initSets[n-i]
            else:
#                print "calc", n-i
                b=capCircs(n-i)
                initSets[n-i]=b
#                print "initSets", initSets
            for ai in a:
                for bi in b:
                    z.add(simp(ai[0]*bi[1]+ai[1]*bi[0], ai[1]*bi[1]))
                    z.add(simp(ai[0]*bi[0], ai[0]*bi[1]+ai[1]*bi[0]))
        if n not in initSets:
#            print "in the end"
            initSets[n]=z
#            print "initSets", initSets
    return z


def ans(x):
    y=capCircs(x)
    z=set([])
    i=1
    while i<=x:
        z=z.union(initSets[i])
        i=i+1
    return z

n=12
z=capCircs(n)
print len(z)
print len(ans(n))

for i in initSets:
    print i, len(initSets[i]), len(ans(i))

