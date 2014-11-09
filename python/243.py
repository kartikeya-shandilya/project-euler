# -*- coding: cp1252 -*-
# create a dict with all numbers as key, their factors as value
# create a list of all factors of all numbers in a given range

from math import sqrt

def sieveOfErat(end):
    if end < 2: return []
    lng=((end>>1)-1+end%2)
    sieve=[True]*(lng+1)  
    for i in xrange(int(sqrt(end))>>1):
        if not sieve[i]: continue
        for j in xrange((i*(i+3)<<1)+3,lng,(i<<1)+3):  
            sieve[j]=False  
    primes=[2]+[(i<<1)+3 for i in xrange(lng) if sieve[i]]
    return primes

primelist=sieveOfErat(50)

min=1
print "objective :",15499/94744.0

i=1
c1=0

wishlist=[2,3,5,7,11,13,17,19,23,2,2,3,3,5]

while 1:
    i*=wishlist[c1]
    coprimes=i
    x=i
    for j in primelist:
        if j>x: break
        if i%j==0:
            x=x/j
            coprimes*=(1-1/(1.0*j))
    fraction=coprimes/(i-1)
    print i,fraction
    if fraction<min:
        den=i;  min=fraction
    if i%10000==0:  print i,den,min
    if fraction<(15499/94744.0):
        print "achieved",i,wishlist[c1]
        break
    c1+=1


