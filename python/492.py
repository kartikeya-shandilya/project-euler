
from math import sqrt

def find_period(p):
	a = 1
	c = 1
	b = {a:c}
	while True:
		c += 1
		a = (6*a*a + 10*a + 3) % p
		if a in b:
			return (b[a], a, c-b[a])
		b[a] = c

def function_a(n, p):
	st, a, period = find_period(p)
	c = 0
	n = (n - st)%period
	while c < n:
		c += 1
		a = (6*a*a + 10*a + 3) % p
	return a

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

def function_B(a, b, c):
	p = next_prime(a-1)
	ans = 0
	while True:
		q = p.next()
		if q > a+b:
			break
		print q,
		a_c = function_a(c, q)
		ans += a_c
		print ans
	return ans

print function_B(10**9,10**2,10**3)


