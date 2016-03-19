
def val(n, p):
    if n < p:
        return 0, 0
    res = val(n/p, p)
    return n/p + res[0], 1 + res[1]


def totient(k):
    return 4 * 10**(k-1)


def mult_elig(n, k, d, elig):
    num_d, max_d = val(n, d)
    ans = 1
    for i in xrange(max_d+1):
        quot = (n/d**i) / 10**k
        remd = (n/d**i) % 10**k
        base = 1
        if quot > 0:
            for j in [x for x in xrange(1, 10**k) if x%10 in elig]:
                base = (base * j) % 10**k
        xtra = 1
        for j in [x for x in xrange(1, remd+1) if x%10 in elig]:
            xtra = (xtra * j) % 10**k
        res = 1
        quot = quot % totient(k)
        for j in xrange(quot):
            res = (res * base) % 10**k
        res = (res * xtra) % 10**k
        ans = (ans * res) % 10**k
    return ans


def pow_2(n, k):
    res = 1
    n = n % totient(k)
    for i in xrange(n):
        res = (res * 2) % 10**k
    return res


def lsd_fact(n, k):
    num_2, max_2 = val(n, 2)
    num_5, max_5 = val(n, 5)
    num_52, max_52 = val(n/5, 2)
    rem_2 = num_2 - num_5 - num_52

    # step-1
    # all 5s removed, with 2's present
    res1 = mult_elig(n/5, k, d=5, elig=[1, 2, 3, 4, 6, 7, 8, 9])

    # step-2
    # all 2s and 5s removed
    res2 = mult_elig(n, k, d=2, elig=[1, 3, 7, 9])

    # step-3
    # remaining powers of 2
    res3 = pow_2(rem_2, k)

    return (res1 * res2 * res3) % 10 ** k

print lsd_fact(10**12, 5)
