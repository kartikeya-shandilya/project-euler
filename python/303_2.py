
def conv(n,b=3):
	ans=[]
	i = 0
	N = n
	while n/b**i>0:
		ans += [N%b]
		N = N/b
		i += 1
	return int(''.join([`i` for i in ans])[::-1])

#for i in xrange(1,1000000):
#	conv(i)

def next_nums():
	digs = [`i` for i in xrange(3)]
	newdigs = ['']
	while 1:
		newdigs2 = []
		for i in digs:
			for j in newdigs:
				if int(i+j)>0:
					yield int(i+j)
				newdigs2.append(i+j)
		newdigs = newdigs2[::]

y = next_nums()
global allnums
allnums = []
for i in xrange(100000000):
	allnums.append(y.next())

def findDiv(n):
	global allnums
	i = 0
	while 1:
		if allnums[i]%n == 0:
			return allnums[i]
		i+=1

ans = 0
for i in xrange(1,1001):
	ans+=findDiv(i)/i

print ans

