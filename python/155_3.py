
from fractions import Fraction
from itertools import product

"""
def combos(n):
    result = {tuple([n])}
    if n == 1:
        return result
    for i in xrange(1, n/2+1):
        tmp = combos(n-i)
        for combo in tmp:
            result.add(tuple(sorted([i]+list(combo))))
    return result
"""


def combos(n):
    result = {tuple([n])}
    if n == 1:
        return result
    for i in xrange(1, n/2+1):
        result.add((i, n-i))
    return result


def parallel(caps):
    return sum(caps)


def serial(caps):
    one = Fraction(1, 1)
    return one/sum(one/x for x in caps)


cap_cache = {1: {Fraction(60)}}
def capacitors(n):
    if n in cap_cache:
        return cap_cache[n]
    all_combos = combos(n)
    result = set()
    for combo in all_combos:
        if list(combo) == [n]:
            continue
        choices = (capacitors(i) for i in combo)
        allprod = product(*choices)
        for prod in allprod:
            result.add(parallel(prod))
            result.add(serial(prod))
    cap_cache[n] = result
    return cap_cache[n]

tmp = capacitors(18)

allres = set()
for i in xrange(1, 19):
    allres = allres.union(cap_cache[i])

print len(allres)
