
import pyprimesieve as pp

numdivs=[0]
for i in xrange(1, 10**8+1):
    num = 1
    for pr, exp in pp.factorize(i):
        num *= (exp + 1)
    numdivs.append(num)

def M(n, k):
    return max(numdivs[n:n+k])

def S(u, k):
    ans = 0
    for n in xrange(1, u-k+2):
        ans += M(n, k)
    return ans

print S(10**8, 10**5)
