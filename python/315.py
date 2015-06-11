
from math import sqrt

num = {0:[1,0,1,1,1,1,1],
	1:[0,0,0,0,1,0,1],
	2:[1,1,1,0,1,1,0],
	3:[1,1,1,0,1,0,1],
	4:[0,1,0,1,1,0,1],
	5:[1,1,1,1,0,0,1],
	6:[1,1,1,1,0,1,1],
	7:[1,0,0,1,1,0,1],
	8:[1,1,1,1,1,1,1],
	9:[1,1,1,1,1,0,1]}

# to count number of segments that are "on" in a digit
def count(i):
	return sum(num[i])
ctdict = {i:count(i) for i in xrange(10)}

# to find the number of segments that are "on" in a number
def aroot(n):
	if n<10:
		return ctdict[n]
	return ctdict[n%10]+aroot(n//10)

# to count number of switches required from one digit to another
def subtr(i, j):
	return sum([num[i][k]!=num[j][k] for k in xrange(7)])
chdict = {(i,j):subtr(i,j) for j in xrange(10) for i in xrange(j+1)}

# to find digital root of a number
kroot = {i:i for i in xrange(10)}
def droot(n):
	if n in kroot:
		return kroot[n]
	kroot[n] = n%10 + droot(n//10)
	return kroot[n]

# memcache maxclock

def maxclock(n):
	ans = aroot(n)
	while True:
		digroot = droot(n)
		if digroot == n:
			ans += aroot(n)
			break
		i = 0
		while True:
			a = (n//10**i)%10
			b = (digroot//10**i)%10
			if n<10**(i+1): 
				ans += ctdict[a]
				break
			if digroot>10**i:
				ans += subtr(min(a,b), max(a,b))
			else:
				ans += ctdict[a]
			i += 1
		n = digroot
	return ans

def samclock(n):
	ans = 0
	while True:
		digroot = droot(n)
		ans += 2*aroot(n)
		if digroot == n:
			break
		n = digroot
	return ans

def next_prime(start):
	current = start
	while True:
		current += 1
		if current<=3:
			yield current
			continue
		elif (current % 2 == 0) or (current % 3 == 0):
			continue
		mult = 1
		while (6*mult - 1) <= sqrt(current):
			if current % (6*mult - 1) == 0:
				current += 1
				break
			elif ((6*mult + 1) <= sqrt(current)) and (current % (6*mult + 1) == 0):
				current += 1
				break
			else:
				mult += 1
		if (6*mult - 1) > sqrt(current):
			yield current

"""
plist = []
N = 2*10**7
sqrt_N = sqrt(N)
slowpr = next_prime(1)
while True:
	p = slowpr.next()
	if p>=sqrt_N:
		break
	plist.append(p)

def fast_prime(start):
	current = start
	while True:
		i = 0
		while plist[i] <= sqrt(current):
			if current % plist[i] == 0:
				break
			i += 1
		if plist[i] > sqrt(current):
			yield current
		current += 1

primes=fast_prime(10**7)
result = 0
while True:
	p = primes.next()
	#print p
	if p == plist[-1]:
		break
	result += samclock(p)
	#print p, result
"""

sieve = __import__('231_sieve')
primes = sieve.sieve(150)
result = 0
for p in primes:
	if p>100:
		s = samclock(p)
		m = maxclock(p)
		print p, s, m
		result += (s-m)
print result

