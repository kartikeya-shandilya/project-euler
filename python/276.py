
from math import ceil

def ceiling(n):
    return int(ceil(n))

def gcd(a,b):
    while 1:
        if b>a: c=a; a=b; b=c
        if b==0:    return 0
        if a%b==0:  return b
        else:       a=a-b

def trgls(n):
	cnt=0
	c_ll=ceiling(n/3.0)
	c_ul=ceiling(n/2.0)
	#print "c range:", c_ll, c_ul
	for c in xrange(c_ll,c_ul):
		b_ll=ceiling(max(c/2.0,(n-c)/2.0))
		b_ul=c+1
		#print "c:", c, "b range:",b_ll, b_ul
		for b in xrange(b_ll,b_ul):
			#print "vars:", n, c, b
			ch1=(gcd(c,b)==1)
			ch2=(gcd(n-c,b)==1)
			ch3=(gcd(n-c-b,c)==1)
			#if ch1 or ch2 or ch3: print c, b, n-c-b
			cnt+=(ch1 or ch2 or ch3)
	return cnt

sm=0
z=500
for i in xrange(1,z+1):
	x=trgls(i); sm+=x;
	#print i,x,sm,"\n","="*20

print z, sm
