from scipy import optimize
from math import sqrt

n = 400/4
unit = sqrt(1/2.)/(n+0.5)
x = [i*unit for i in xrange(1,n+1)]

def area(x):
	x = list(x)
	y = [sqrt(1-i**2) for i in x]
	x2 = y[::-1]
	y2 = x[::-1]
	x.extend(x2)
	y.extend(y2)
	total = x[0]
	for i in xrange(len(x)-1):
		total += (x[i+1]-x[i])*y[i]
	total += (1-x[-1])*y[-1]
	#print 4*total
	return 4*total

guess = optimize.minimize(area, x, 
		bounds = [(0,sqrt(1/2.))]*n, tol=1e-11, options={'maxiter':10000},
		constraints = ({'type': 'ineq', 'fun': lambda x:  x[i+1] - x[i]} for i in xrange(n-1)))

print guess

