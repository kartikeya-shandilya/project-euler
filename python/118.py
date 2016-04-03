
from math import sqrt
from collections import defaultdict, Counter
from itertools import permutations

def is_prime(n):
	if n<=1:
		return False
	elif n==2 or n==3:
		return True
	elif n%2 == 0:
		return False
	else:
		flag = True
		for i in xrange(3,int(sqrt(n))+1):
			if n%i == 0:
				flag = False
				break
		return flag

def segment_primes(digs, primes=[]):
	if not len(digs):
		print sorted(primes)
	else:
		for i in range(1,len(digs)+1):
			j = int(''.join([repr(k) for k in digs[:i]]))
			if is_prime(j):
				segment_primes(digs[i:], primes+[j])

#from code import interact; interact(local=dict(globals(), **locals()))

perms = permutations(range(1,10))
for i in xrange(362880):
	segment_primes(perms.next())

