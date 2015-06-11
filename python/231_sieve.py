
import math

def sieve(n):
	length=(n/6)*2
	sieve=[True]*(length+1)
	#print "-",[2,3]+[(6*((x+1)/2)+((-1)**(x))) for x in xrange(1,len(sieve)) if sieve[x]]
	for i in xrange(1,length):
		if (6*((i+1)/2)+((-1)**(i)))**2>n: break
		#print "loop",i,6*((i+1)/2)+((-1)**(i))
		if not sieve[i]: continue
		for j in xrange((6*((i+1)/2)+((-1)**(i)))**2, n, 2*(6*((i+1)/2)+((-1)**(i)))):
			#print i,6*((i+1)/2)+((-1)**(i)),j
			if j%6*(6-j%6)==5: sieve[(j-1)/3]=False
			#print "-",[2,3]+[(6*((x+1)/2)+((-1)**(x))) for x in xrange(1,len(sieve)) if sieve[x]]
	primes=[2,3]+[(6*((x+1)/2)+((-1)**(x))) for x in xrange(1,len(sieve)) if sieve[x]]
	return primes

#print len(sieve(20000000))

