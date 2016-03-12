from collections import defaultdict

def mult(a, b):
    res = defaultdict(int)
    for i in a:
        for j in b:
            res[i+j] = (res[i+j] + a[i]*b[j])
    return res

cache_B = {}
def B(n, k):
    if (n, k) in cache_B:
        return cache_B[(n, k)]
    base = {i: 1 for i in xrange(10)}
    res = base.copy()
    for i in xrange(k-1):
        res = mult(res, base)
    cache_B[(n, k)] = res[n] if n in res else 0
    return cache_B[(n, k)]

cache_A = {}
def A(n, k):
    if (n, k) in cache_A:
        return cache_A[(n, k)]
    if k == 1:
        return 1
    l = min(n, 9)
    cache_A[(n, k)] = sum([B(n-i, k-1) for i in range(1, l+1)])
    return cache_A[(n, k)]

def C(k):
    return sum([A(n, k) * B(n, k) for n in xrange(1, 9*k+1)])

def D(n, k):
    return (B(n, k) * (10**k - 1) * n) / (9 * k)

def Q(k):
    return sum([A(n, k) * D(n, k) for n in xrange(1, 9*k+1)])

# & the sum of second half be P(k): k digits
def E(n, k):
    if k==1:
        return n
    l = min(n, 9)
    return sum([B(n-i, k-1) * 10**(k-1) * i + D(n-i, k-1) for i in xrange(1, l+1)])

def P(k):
    return sum([B(n, k) * E(n, k) for n in range(1, 9*k+1)])

def S(k):
    if k==1:
        return 45
    elif k%2==0:
        return (P(k/2)*10**(k/2) + Q(k/2))
    else:
        return (10*P(k/2)*10**(1+k/2) + C(k/2)*45*10**(k/2) + 10*Q(k/2))

def T(k):
    return sum([S(i) for i in xrange(1, k+1)])

print T(47)%3**15

"""
def sod(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

def BAL(k, flag=True):
    res1 = defaultdict(int)
    res2 = defaultdict(int)
    total = 0
    idx1 = idx2 = k/2
    if k%2:
        idx1 = 1 + k/2
        idx2 = k/2
    for n in xrange(10**(k-1), 10**k):
        num = str(n)
        sodig1 = sod(num[:idx1])
        sodig2 = sod(num[idx2:])
        if sodig1==sodig2:
            total += n
            res1[sodig1] += int(num[:idx1])
            res2[sodig2] += int(num[idx2:])
    return total
"""
