#!/usr/bin/python

import math

def term(n):
    while 1:
        if   (n%2==0): n=n/2
        elif (n%5==0): n=n/5
        else : break
    if (n==1): return -1
    else:      return 1

def gcd(a,b):
    if   a==b: return a
    elif a >b: return gcd(a-b,b)
    else :     return gcd(a,b-a)

sm=0
for i in range(5,10001):
    a=int(i/(1.0*math.e))
    j=a*math.log((1.0*i)/a)
    k=(a+1)*math.log((1.0*i)/(a+1))
    if j>k:
        add=i*term(a/gcd(a,i))
    else:
        add=i*term((a+1)/gcd(a+1,i))
    sm=sm+add
    
print sm
