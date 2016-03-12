
import pyprimesieve as pp


def permutations(n, rem):
    for i in xrange(len(n)+1):
        newnum = n[:i] + rem[0] + n[i:]
        if len(rem) == 1:
            yield newnum
        else:
            for num in permutations(newnum, rem[1:]):
                yield num


def isprime(n):
    fact = pp.factorize(n)
    return len(fact)==1 and fact[0][1]==1


def nums_N(n, c, d):
    base = str(d)*c
    rem = "abcdef"[:n-c]
    for num in permutations(base, rem):
        for i in xrange(10**(n-c)):
            num_ = num
            rep = str(i).zfill(n-c)
            for j in xrange(len(rep)):
                num_ = num_.replace(rem[j], rep[j])
            num_ = int(num_)
            if num_>10**(n-1) and isprime(num_):
                yield num_


def sum_S(n, d):
    res = 0
    c = n-1
    primes = []
    while not len(primes):
        primes = list(set(list(nums_N(n, c, d))))
        c = c-1
    print "digit: %s, #max rep: %s, #primes: %s, sum_primes: %s" % (d, c+1, len(primes), sum(primes))
    res += sum(primes)
    return res

ans = 0
for d in xrange(10):
    ans += sum_S(10, d)
print "ans: %s" % ans
