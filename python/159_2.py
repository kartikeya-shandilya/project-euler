
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


def drs(n):
    res = (n % 9)
    return [res, 9][res == 0]


mdrs_cache = {}
def mdrs(n):
    if n == 1:
        return 0
    if n in mdrs_cache:
        return mdrs_cache[n]
    my_divisors = sorted(list(divisors(n)))
    if len(my_divisors)==2:
        return drs(n)
    res = 0
    for div in my_divisors[1:]:
        res = max(res, drs(div) + mdrs(n/div))
    mdrs_cache[n] = res
    return res


res = 0
for n in xrange(1, 10**4):
    res += mdrs(n)
print res
