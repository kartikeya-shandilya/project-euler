
import pyprimesieve as pp


def val_p(k, p):
    res = 0
    i = 1
    while k/p**i:
        res += k/p**i
        i += 1
    return res


"""
def get_k(p, a, l):
    return a*(p**l)*(p-1)/(p**l-1)

"""


def bin_search(low_k, high_k, p, a):
    mid_k = (low_k + high_k)/2
    if val_p(mid_k, p)>=a and val_p(mid_k-1, p)<a:
        return mid_k
    elif val_p(mid_k, p)<a:
        return bin_search(mid_k+1, high_k, p, a)
    else:
        return bin_search(low_k, mid_k, p, a)


"""
def find_low_high(p, a):
    l = 2
    high_k = get_k(p, a, 1)
    while True:
        tmp_k = get_k(p, a, l)
        if val_p(tmp_k, p) >= a:
            high_k = tmp_k
        else:
            low_k = tmp_k
            break
        l += 1
    return low_k, high_k
"""

def find_low_high(p, a):
    low = min_k(p, a-1)
    return low, low+p


min_k_cache = {}
def min_k(p, a):
    if a<=p:
        return a*p
    if a>1 and (p, a) in min_k_cache:
        return min_k_cache[(p, a)]
    low, high = find_low_high(p, a)
    k = bin_search(low, high, p, a)
    if a>1:
        min_k_cache[(p, a)] = k
    return k


def min_fact(n):
    fact = pp.factorize(n)
    res = 1
    for p, a in fact:
        res = max(res, min_k(p, a))
    return res


#from code import interact; interact(local=dict(globals(), **locals()))
print sum([min_fact(i) for i in xrange(2, 10**8+1)])
