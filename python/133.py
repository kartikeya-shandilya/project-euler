
import pyprimesieve as pp

def rep_rem(k, n):
    r = 0
    k = 10**k
    while k:
        r = (10 * r + 1) % n
        k -= 1
    return r

def check_rems(n):
    rems = set()
    i = 1
    while True:
        rem = rep_rem(i, n)
        if rem == 0:
            return False
        if rem in rems:
            return n
        else:
            rems.add(rem)
        i += 1

for i in xrange(2, 100):
    fact = pp.factorize(i)
    if len(fact)==1 and fact[0][1]==1:
        if check_rems(i) == False:
            print i
