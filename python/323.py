
from operator import mul

nCk = lambda n,k: int(round(
    reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)
))

ans = [2]

for i in xrange(2,33):
    tmp = 2.0/2**i
    for j in xrange(len(ans)):
        tmp += nCk(i,j+1)*(1.0/2**i)*(1+ans[j])
    new = (1/(1-1.0/2**i))*tmp
    print i, new
    ans.append(new)

