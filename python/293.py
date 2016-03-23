
from math import sqrt, log
import pyprimesieve as pp

import sys
sys.setrecursionlimit(5000)


def max_primepow(n, prime):
    if n < prime:
        return 0
    return int(log(n)/log(prime))


myprimes = set(pp.primes(10**9))
def gen_admissible(n, prodprimes=1, lastprime=1, admiss=[1], valids=[1]):
    nextprime = None
    for num in xrange(lastprime+1, int(sqrt(n))+1):
        if num in myprimes:
            nextprime = num
            prodprimes = prodprimes * nextprime
            break
    if not nextprime:
        return admiss
    else:
        newadmiss = []
        for base in sorted(valids):
            max_pow = max_primepow(n/base, nextprime)
            if not max_pow:
                break
            newadmiss += [base*nextprime**i for i in xrange(1, max_pow+1)]
        admiss += newadmiss
        if 1 in admiss:
            admiss.remove(1)
        return gen_admissible(n, prodprimes, nextprime, admiss, newadmiss)


def pseudo_fort(n):
    num = n+3
    while True:
        if num in myprimes:
            break
        num += 1
    return num - n


all_admiss = gen_admissible(10**9)
all_psfort = set()
for i, num in enumerate(all_admiss):
    psfort = pseudo_fort(num)
    all_psfort.add(psfort)

print sum(all_psfort)
