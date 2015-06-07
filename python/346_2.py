
from collections import defaultdict
from math import sqrt,ceil

lim = 10**12
lrt = int(ceil(sqrt(lim)))

cache = defaultdict(list)
for a in xrange(2,lrt+1):
	m = 1
	s = 1
	while a**m<lim:
		s += a**m
		m += 1
		if s<lim:
			cache[s].append(a)

print 1+sum([key for key in cache if len(cache[key])>1 or key>lrt+1])

