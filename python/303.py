
from math import ceil

def isValid(n,digs=['0','1','2']):
	return all(i in digs for i in `n`)

def getFirstValid(n, minChk, maxChk):
	#print 'getFirstValid:', n, minChk, maxChk
	i = minChk
	while i <= maxChk+1:
		if isValid(i): return i
		i += n
	return None

def findValid(n, j):
	cnt = 0
	while cnt < 15:
		x = 10**j
		y = getFirstValid(n, int(x*1.0/n)*n, 3*x)
		if y:
			return y
		else:
			j += 1
			cnt += 1

j=0
ans=0
for i in xrange(1,101):
	if i>=3*10**j:
		j+=1
	if isValid(i):
		num = i
	else:
		num = findValid(i,j)
	print i, num
	ans+=num/i

print 'ans =', ans

