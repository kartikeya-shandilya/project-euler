
import pyprimesieve as pp

from itertools import product, combinations as combos
from collections import Counter
from operator import mul

"""res = 0
for i in xrange(1, 10**5+1):
    fac = pp.factorize(i)
    res += sum([j for i, j in fac])
print res
"""

cache = {}
def partial_orders(n):
    fac = pp.factorize(n)
    chk = tuple(sorted([j for i, j in fac]))
    if chk in cache:
        return cache[chk]
    fac = [[i]*j for i, j in fac]
    res = [1]
    while fac:
        primes = [p[0] for p in fac if p!=[]]
        print 'primes:', primes
        print 'fac: before:', fac
        fac = [p[1:] for p in fac if len(p)>1]
        print 'fac: after:', fac
        newres = list(product(primes, res))
        newres = list(set([reduce(mul, i) for i in newres]))
        res = newres
        print res
    cache[chk] = len(res)
    return len(res)

cache = {}
def perfect_orders(n):
    fac = pp.factorize(n)
    chk = tuple(sorted([j for i, j in fac]))
    if chk in cache:
        return cache[chk]
    facs = [range(j+1) for i, j in fac]
    divs = product(*facs)
    divs = [sum(div) for div in divs]
    res = Counter(divs).most_common(1)[-1][-1]
    cache[chk] = res
    return res


if __name__ == "__main__":
    res = 0
    for i in xrange(1, 10**8+1):
        res += perfect_orders(i)
    print res
