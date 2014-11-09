
import math

def primes(n):
	x,y=int(math.sqrt(n)),n
	list=[]
	for i in xrange(2,x+1):
		if i not in list and y%i==0:
			list.append(i)
			while y%i==0:	y=y/i
	return list

def totient(n):
	y=n
	list=primes(n)
	for i in list:
		y=(y*(i-1))/i
	return y

x=6
z=10**x
l=1777
#l=17
k=1855
#k=18
totlist=[z]

for i in xrange(k):
	z=totient(z)
	totlist.append(z)
print totlist

z=10**x
rem=l
for i in xrange(k):
	print i," ",l%totlist[-2-i],"^",rem%totlist[-1-i],"-",rem
	rem=(l%totlist[-2-i])**(rem%totlist[-1-i])
	print rem,"\n_"

print rem,z,rem%z


