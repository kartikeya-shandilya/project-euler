
def nCr(n, r, mod=10**9):
	result = 1
	y = 1
	for x in xrange(n, r, -1):
		result = (result*x/y)%mod
		y += 1
	return result

def f(x, mod=10**9):
	result = 0
	for i in xrange(
