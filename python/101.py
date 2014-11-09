
def f(n):
    return 1 - n + n**(2) - n**(3) + n**(4) - n**(5) + n**(6) - n**(7) + n**(8) - n**(9) + n**(10)

#def f(n):
#	return n**3

def diff(x):
	y=[]
	for i in xrange(len(x)-1):
		y.append(x[i+1]-x[i])
	return y

def predict(x):
	if len(x)==1:
		return x[0]
	else:
		return x[-1]+predict(diff(x))

x=[]
sum=0 
for i in xrange(1,12):
	print "iteration", i
	y =	f(i)
	print "y", y
	x.append(y)
	print "x", x
	z = predict(x)
	print "pred", z
	sum = sum + z
	print "---------------"

print sum - z

