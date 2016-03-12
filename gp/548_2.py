
import eulerlib
import sys

sys.setrecursionlimit(2000)
numtheory = eulerlib.Divisors(10**8)
gazinga_cache = {1: 1}
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


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


def newidx(combo, nmax=10**9):
    newcombo = [1]*(len(combo)+1)
    return len(combo), newcombo


def match(x, y):
    fact_x = numtheory.prime_factors(x)
    fact_y = numtheory.prime_factors(y)
    exp_x = sorted([elm[1] for elm in fact_x])
    exp_y = sorted([elm[1] for elm in fact_y])
    return exp_x == exp_y


def find(combo, nmax=10**9):
    idx, newcombo = firstidx(combo)
    res = isvalid(newcombo, nmax)
    if res[0]:
        gznga = gazinga(res[1])
        if match(res[1], gznga): print gznga
        find(newcombo, nmax)
    else:
        idx, newcombo = newidx(combo, nmax)
        res = isvalid(newcombo, nmax)
        if res[0]:
            gznga = gazinga(res[1])
            if match(res[1], gznga): print gznga
            find(newcombo, nmax)


def isprimepower(n):
    facts = numtheory.prime_factors(n)
    return len(facts) == 1


def gazinga(n):
    if n in gazinga_cache:
        return gazinga_cache[n]
    elif isprimepower(n):
        prime, exponent = numtheory.prime_factors(n)[0]
        gazinga_cache[n] = 2**(exponent-1)
        return 2**(exponent-1)
    else:
        res = 0
        for d in numtheory.divisors(n):
            if d < n:
                res += gazinga(d)
        gazinga_cache[n] = res
        return gazinga_cache[n]


find([1], 10**5)
