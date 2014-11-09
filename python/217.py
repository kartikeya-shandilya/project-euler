
def poly(a, b):
    c = []
    for k in xrange(len(a)+len(b)-1):
        c.append(0)
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            c[i+j] += a[i]*b[j]
    return c

def summ(a, b, c):
    print "======", c, len(a), len(b)
    d = 0
    for i in xrange(1, len(a)):
        d += (1+10**(c/2))*i*a[i]*b[i]*(10**(c%2))
    if c%2:
        d += 45*10**((c+1)/2)*a[i]*b[i]
    return d

init = a = [0,1,1,1,1,1,1,1,1,1]
rept = b = [1,1,1,1,1,1,1,1,1,1]

x = 45

for i in xrange(2, 6):
    x += summ(a, b, i)
    print x, a, b
    if not i%2:
        a = poly(a, rept)
        b = poly(b, rept)

