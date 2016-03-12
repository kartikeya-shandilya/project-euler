
import pyprimesieve as pp

from itertools import product
from operator import mul


def divisors(n):
    fact = pp.factorize(n)
    divgen = []
    for elm in fact:
        pr, expon = elm
        divgen.append([pr**i for i in xrange(expon+1)])
    for nums in product(*divgen):
        yield reduce(mul, nums)


fact_cache = {}
def factorizations(n):
    if n == 1:
        return {(1,)}
    if n in fact_cache:
        return fact_cache[n]
    res = set()
    for div in sorted(list(divisors(n)))[1:]:
        facts = factorizations(n/div)
        facts = {tuple(sorted(list(f)+[div])) for f in facts}
        res = res.union(facts)
    fact_cache[n] = res
    return res


def drs(facts):
    res = 0
    for f in facts[1:]:
        res += (f % 9)
    return [res, 9][res == 0]


def mdrs(n):
    res = 0
    for fact in factorizations(n):
        res = max(res, drs(fact))
    return res

res = 0
for n in xrange(1, 10**4):
    res += mdrs(n)
print res
