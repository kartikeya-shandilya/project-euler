import math

def primes(n):
	global dict
	global rangecheck
	y=n
	for i in rangecheck:
		if i>n: break
		if not dict.has_key(i) and y%i==0:
			dict[i]=0
		while y%i==0 and y>1:
			dict[i]+=1
			y=y/i
	return dict

st=20000000
en=19990000

rangecheck=[2,3]
for x in xrange(5,st,6):
	rangecheck.append(x)
	rangecheck.append(x+2)

dict={}

for i in range(st,en,-1):
	primes(i)

print dict

