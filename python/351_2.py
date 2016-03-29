
from fractions import Fraction

dot_cache = set()
def dots(n):
    parity = n%2
    for i in xrange(n/2+1):
        frac = Fraction(2*i+parity, 2*n)
        if frac not in dot_cache:
            dot_cache.add(frac)
    return None

n = 3
for i in xrange(1, n+1):
    dots(i)
print 3*n*(n+1)
print 6*len(dot_cache)
