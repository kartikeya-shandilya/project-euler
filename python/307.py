
from math import log, exp
from decimal import *

getcontext().prec=40

#def Decimal(x):
#    return x*1.0

def logbase(n, k):
    res = 0
    for i in xrange(k/2 + k%2):
        res += Decimal(log((n - i) * Decimal(1)/(k/2 + k%2 - i)))
        res += Decimal(log((k - i) * (i + Decimal(1)) / Decimal(2)))
    if k % 2:
        res += Decimal(log(2))         # to remove 2! from denominator
        res -= Decimal(log(k/2))       # to remove double count in the numerator
    res -= Decimal(k*log(n))
    return res


def prob_2orless(n, k):
    B_o = logbase(n, k)
    k_2 = k/2 + k%2
    result = Decimal(exp(B_o))
    print 'base : Prob = %s' % (result)
    for i in xrange(1, k/2 + 1):
        B_i = B_o + Decimal(log((n + Decimal(1) - k_2 - i)/(k_2 + i)))
        B_i = B_i + Decimal(log(2 * (k_2 + Decimal(1) - i) * (k_2 + i)))
        B_i = B_i - Decimal(log((k%2 + 2*i) * (k%2 + Decimal(1)) * (k%2 + 2*i - 1)))
        B_o = B_i
        if i>9900:
            print 'step %s : Prob = %s' % (i, exp(B_o))
        result += Decimal(exp(B_o))
    return result


print 1 - prob_2orless(1000000, 20000)
