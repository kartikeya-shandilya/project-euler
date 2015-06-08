
from collections import defaultdict, OrderedDict

c = defaultdict(int)
for sq in range(1,40000):
	for cb in range(1,2000):
		num = sq**2 + cb**3
		if str(num)==str(num)[::-1]:
			c[sq**2 + cb**3] += 1

d = {i:c[i] for i in c if c[i]==4}
d = OrderedDict(sorted(d.items()))

print sum([i for i in d.keys()[:5]])


