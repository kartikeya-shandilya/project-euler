
f_cache = {}
def f(k, n):
	if (k, n) in f_cache:
		return f_cache[(k, n)]
	elif n==0:
		return 1
	else:
		a0 = lambda k=k, n=n: n%k
		n1 = lambda k=k, n=n: n/k
		n2 = lambda k=k, n=n: (n/k)/k

		res = 0
		for i in xrange(n2()):
			res = (res + (k*n1() - k*(k+1)/2)*f(k, i)) % (10**9+7)
		res = k*res % (10**9+7)
		res = (res + (1+a0())*f(k, n1())) % (10**9+7)
		f_cache[(k, n)] = res
		return res


"""
def f(k, n):
	if (k, n) in f_cache:
		return f_cache[(k, n)]
	elif n==0:
		return 1
	else:
		res = 0
		for i in xrange(n/k):
			res += k*f(k, i)
		res = (res + (1+n%k)*f(k, n/k)) % (10**9+7)
		f_cache[(k, n)] = res
		return res
"""
