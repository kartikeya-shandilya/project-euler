
global g
g={1:1,2:2}

def golomb(n):
    if n in g: return g[n]
    i=1; j=1;
    if n<3: return n
    while 1:
        if i==n:
            if n not in g:
                g[n]=j
            return j
        elif i>n:
            if n not in g:
                g[n]=j-1
            return j-1
        i+=golomb(j)
        j+=1

sm=0;
for i in xrange(1,10**3+1):
    sm+=golomb(i**3)

print sm
