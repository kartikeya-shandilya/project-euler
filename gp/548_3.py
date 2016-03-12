
import pyprimesieve as pp
import sys

from itertools import product
from operator import mul

sys.setrecursionlimit(2000)
gazinga_cache = {1: 1}
prime = pp.primes(45)


def isvalid(combo, nmax=10**9):
    num = 1
    for i, n in enumerate(combo):
        num = num * prime[i]**n
    return num < nmax, num


def firstidx(combo):
    idx = 0
    for i in xrange(len(combo)-1, 0, -1):
        if combo[i] < combo[i-1]:
            idx = i
            break
    combo[idx] += 1
    newcombo = combo[:idx+1] + [1]*len(combo[idx+1:])
    return idx, newcombo


def secondidx(combo, nmax=10**9):
    newcombo = [combo[0]+1] + [1]*(len(combo)-1)
    return len(combo), newcombo


def thirdidx(combo, nmax=10**9):
    newcombo = [1]*(len(combo)+1)
    return len(combo), newcombo


def match(x, y):
    if y > 10**16:
        return False
    fact_x = pp.factorize(x)
    fact_y = pp.factorize(y)
    exp_x = sorted([elm[1] for elm in fact_x])
    exp_y = sorted([elm[1] for elm in fact_y])
    return exp_x == exp_y


def find(combo, nmax=10**9):
    idx, newcombo = firstidx(combo)
    res = isvalid(newcombo, nmax)
    if res[0]:
        gznga = gazinga(res[1])
        print newcombo[::-1]
        #if match(res[1], gznga): print gznga
        find(newcombo, nmax)
    else:
        idx, newcombo = secondidx(combo, nmax)
        res = isvalid(newcombo, nmax)
        if res[0]:
            gznga = gazinga(res[1])
            print newcombo[::-1]
            #if match(res[1], gznga): print gznga
            find(newcombo, nmax)
        else:
            idx, newcombo = thirdidx(combo, nmax)
            res = isvalid(newcombo, nmax)
            if res[0]:
                gznga = gazinga(res[1])
                print newcombo[::-1]
                #if match(res[1], gznga): print gznga
                find(newcombo, nmax)


def isprimepower(n):
    facts = pp.factorize(n)
    return len(facts) == 1


def divisors(n):
    fact = pp.factorize(n)
    divgen = []
    for elm in fact:
        pr, expon = elm
        divgen.append([pr**i for i in xrange(expon+1)])
    for nums in product(*divgen):
        yield reduce(mul, nums)


def gazinga(n, nmax=10**9):
    if n in gazinga_cache:
        return gazinga_cache[n]
    elif isprimepower(n):
        prime, exponent = pp.factorize(n)[0]
        gazinga_cache[n] = 2**(exponent-1)
        return 2**(exponent-1)
    else:
        res = 0
        for d in divisors(n):
            if d < n:
                res += gazinga(d, nmax=10**9)
                if res > nmax:
                    break
        gazinga_cache[n] = res
        return gazinga_cache[n]

# find([1], 5*10**3)


def newidx(combo, nmax=10**9):
    # get indices that can be increased
    idcs = [0]+[i for i in xrange(1, len(combo)) if combo[i] < combo[i-1]]
    for idx in idcs[::-1]:
        newcombo = combo[:idx] + [combo[idx]+1] + [1]*len(combo[idx+1:])
        if isvalid(newcombo, nmax)[0]:
            return newcombo
    # finally add more elms
    newcombo = [1]*(len(combo)+1)
    if isvalid(newcombo, nmax)[0]:
        return newcombo


def newfind(combo, nmax=10**9):
    newcombo = combo
    while newcombo:
        res = isvalid(newcombo, nmax)
        gznga = gazinga(res[1], nmax)
        if gznga<nmax and match(res[1], gznga): print gznga
        newcombo = newidx(newcombo, nmax)


newfind([1], 10**14)
