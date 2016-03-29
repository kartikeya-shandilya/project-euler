
from collections import defaultdict


def rng(last, prime, modulus=50515093):
    if not last:
        last = 290797
    s = last**2 % modulus
    return s, s % prime


def exp_modulo(p, n, modulus):
    if n == 0:
        return 1
    if n == 1:
        return p
    quot = n / 2
    rem = n % 2
    result = exp_modulo(p, quot, modulus)**2 % modulus
    if rem:
        result = (result * exp_modulo(p, rem, modulus)) % modulus
    return result


def calc_value(T, n, p, sumprimepow, modulus=1):
    res = defaultdict(float)
    last = T * 1.
    cnt = n
    while cnt:
        res[n-cnt] = last * (1./p)
        last = last * (1./p)
        cnt -= 1
    return res


def add_dicts(dict1, dict2):
    allkeys = set(dict1).union(set(dict2))
    fulldict = defaultdict(float)
    for key in allkeys:
        fulldict[key] = dict1[key] + dict2[key]
    return fulldict


def compute_NF(p, q, modulus=1):
    last = None
    res = defaultdict(float)
    for n in xrange(0, q+1):
        T = rng(last, p)
        newdict = calc_value(T, n, p, modulus)
        res = add_dicts(res, newdict)
    return sum(int(i) % modulus for i in res.values())


# print compute_NF(3, 10000, 3**20)
