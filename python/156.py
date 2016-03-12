
from collections import defaultdict


def f(n, d):
    num = str(n)[::-1]
    res = 0
    for i in xrange(1, len(num)+1):
        tmp = (n/10**(i)) * 10**(i-1)
        if int(num[i-1])==d:
            tmp += (1 + n%(10**(i-1)))
        elif int(num[i-1])>d:
            tmp += 10**(i-1)
        res += tmp
    return res

def bin_search(a, b, d):
    # search in range a and b inclusive
    mid = (a+b)/2
    low = f(a, d)
    val = f(mid, d)
    hi = f(b, d)
    results = set()
    if not (val<a or low>mid) and (b-a)>1:
        result = bin_search(a, mid, d)
        if len(result):
            results = results.union(result)
    if not (val>b or hi<mid) and (b-a)>1:
        result = bin_search(mid, b, d)
        if len(result):
            results = results.union(result)
    if val==mid:
        result = {mid}
        if len(result):
            results = results.union(result)
    return results


maxlim = 100
results = []
res = defaultdict(list)
for d in range(1, 10):
    tmp = list(bin_search(1, 10**maxlim, d))
    for elm in tmp:
        res[elm].append(d)
    results = results + tmp
print sum(results)

for num, digs in res.iteritems():
    if len(digs)>1:
        print num, digs

from code import interact; interact(local=dict(globals(), **locals()))
