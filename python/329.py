
import pyprimesieve as pp
primes = set(pp.primes(500))

from collections import defaultdict
from fractions import Fraction as F


def shoutprob(yelp, k):
    res = F(1, 3) * (F(1) + F(k in primes))
    if yelp == 'P':
        return res
    else:
        return F(1) - res


def getjumps(k, n=500):
    if k == 1:
        return {k+1: F(1)}
    elif k == n:
        return {k-1: F(1)}
    else:
        return {k-1: F(1, 2), k+1: F(1, 2)}


def movefrog(yelp, possib):
    newpossib = defaultdict(F)
    for k, prob in possib.iteritems():
        for j, jprob in getjumps(k).iteritems():
            newpossib[j] += prob*shoutprob(yelp, k)*jprob
    return newpossib

possib = {k: F(1, 500) for k in range(1, 501)}
for yelp in 'PPPPNNPPPNPPNPN':
    possib = movefrog(yelp, possib)
print sum(possib.values())
