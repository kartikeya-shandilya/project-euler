
def combs(x,y):
	# fac(x+y) / {fac(x) * fac(y)}
	sum=x+y
	fac1=1
	fac2=1
	for i in xrange(1,x+1):
		fac1*=sum
		fac2*=x
		sum-=1
		x-=1
	return (fac1/fac2)

n=6
arr=[]
for i in xrange(1,2+n/2):
	arr.append(combs(i,n-i-i+1))

print arr

