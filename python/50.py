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

limit=1000000

primelist=sieveOfErat(limit)
l=len(primelist)

cnt=0
maxcnt=0
maxprm=0
for i in xrange(l):
    sum=primelist[i]
    cnt=1
    for j in xrange(i+1,l):
        #print i,j,sum,primelist[j]
        if sum<limit-primelist[j]:
            sum=sum+primelist[j]
            cnt=cnt+1
        else:
            break
        try:
            if primelist.index(sum)>0:
                if cnt>maxcnt:
                    maxcnt=cnt
                    maxprm=sum
        except:
            continue
        #print "max",maxprm,maxcnt
    #print

print "max",maxprm,maxcnt

