
num=[17,  78,  19,  23,  29,  77,  95,  77,  1,  11,  13,  15,  1,  55]
den=[91,  85,  51,  38,  33,  29,  23,  19,  17,  13,  11,  2,  7,  1 ]
lng=len(num)

def fractran(n):
	for i in xrange(lng):
		if n%den[i]==0:
			return num[i]*n/den[i]

x=2; z=0;
for i in xrange(10000):
	y=x
	while(y%2==0): y/=2
	if y==1: print x,i,z
	z=x; x=fractran(x)
