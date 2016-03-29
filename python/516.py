
from math import log
import pyprimesieve as pp

import sys
sys.setrecursionlimit(5000)


def max_primepow(n, prime):
    if n < prime:
        return 0
    return int(log(n)/log(prime))


myprimes = set(pp.primes(10))
def gen_admissible(n, prodprimes=1, lastprime=1, admiss=[1]):
    nextprime = None
    for num in xrange(lastprime+1, 6):
        if num in {2, 3, 5}:
            nextprime = num
            prodprimes = prodprimes * nextprime
            break
    if not nextprime:
        return admiss
    else:
        newadmiss = []
        for base in sorted(admiss):
            max_pow = max_primepow(n/base, nextprime)
            if not max_pow:
                break
            newadmiss += [base*nextprime**i for i in xrange(1, max_pow+1)]
        admiss += newadmiss
        return gen_admissible(n, prodprimes, nextprime, admiss)


all_admiss = gen_admissible(10**12)
print sorted(all_admiss)
