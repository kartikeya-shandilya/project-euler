# -*- coding: cp1252 -*-
# create a dict with all numbers as key, their factors as value
# create a list of all factors of all numbers in a given range

from math import sqrt

def sieveOfErat(end):
    if end < 2: return []
    lng=((end>>1)-1+end%2)
    #print lng
    sieve=[True]*(lng+1)  
    for i in xrange(int(sqrt(end))>>1):
        if not sieve[i]: continue
        for j in xrange((i*(i+3)<<1)+3,lng,(i<<1)+3):  
            sieve[j]=False  
    primes=[2]+[(i<<1)+3 for i in xrange(lng) if sieve[i]]
    return primes

limit=10000000

primelist=sieveOfErat(limit)
l=len(primelist)

f=open("./primes.txt","w")

for i in primelist:
    f.write(`i`+"\n")
