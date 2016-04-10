
# p(a, b) = probability of win for A, given A's turn and state-(a, b)
# q(a, b) = probability of win for B, given B's turn and state-(a, b)

p_cache = {}
def p(a, b):
    if (a, b) in p_cache:
        return p_cache[(a, b)]
    if a >= 100 and b < 100:
        res = 1
    elif b >= 100:
        res = 0
    else:
        res = 1 - (q(a, b) + q(a+1, b))/2.
    p_cache[(a, b)] = res
    return res


q_cache = {}
def q(a, b):
    if (a, b) in q_cache:
        return q_cache[(a, b)]
    if a < 100 and b >= 100:
        res = 1
    elif a >= 100:
        res = 0
    else:
        res = 0
        for t in xrange(1, 101-b):
            res = max(res, q_(a, b, t))
    q_cache[(a, b)] = res
    return res


def q_(a, b, t):
    res = (2**t - 1) * q(a+1, b)
    res += 2 * (1 - p(a, b+2**(t-1)))
    res /= (1. + 2**t)
    return res
