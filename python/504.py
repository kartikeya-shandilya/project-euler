
gcd_cache = {}
def gcd(a, b):
    a, b = min(a, b), max(a, b)
    if (a, b) in gcd_cache:
        return gcd_cache[(a, b)]
    if b % a == 0:
        return a
    gcd_cache[(a, b)] = gcd(a, b-a)
    return gcd_cache[(a, b)]


triangle_cache = {}
def triangle(a, b):
    a, b = min(a, b), max(a, b)
    if (a, b) in triangle_cache:
        return triangle_cache[(a, b)]
    allpts = (a+1)*(b+1)
    res = (allpts - gcd(a, b) - 1)/2 - (a + b) + 1
    triangle_cache[(a, b)] = res
    return res


def quadilateral(a, b, c, d):
    res = 0
    res += triangle(a, b)
    res += triangle(c, d)
    res += triangle(a, c)
    res += triangle(b, d)
    res += (a + b + c + d)
    res -= 3
    return res


def is_sq(n):
    from math import sqrt
    return sqrt(n) == int(sqrt(n))


def sq_quads(max_n):
    all_tr = [(a, b) for b in xrange(1, max_n+1) for a in xrange(1, b+1)]
    res = 0
    for a, b in all_tr:
        for c, d in all_tr:
            tmp = is_sq(quadilateral(a, b, c, d))
            if a != b:
                tmp += is_sq(quadilateral(b, a, c, d))
            if c != d:
                tmp += is_sq(quadilateral(a, b, d, c))
            if a != b and c != d:
                tmp += is_sq(quadilateral(b, a, d, c))
            res += tmp
    return res

# populate triangles
max_n = 100
for b in xrange(1, max_n+1):
    for a in xrange(1, b+1):
        triangle(a, b)

print sq_quads(50)
