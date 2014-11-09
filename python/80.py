# -*- coding: cp1252 -*-
# create a dict with all numbers as key, their factors as value
# create a list of all factors of all numbers in a given range

from math import sqrt

def num(arr):
    ans=arr[1]
    k=1
    for i in xrange(len(arr)-1):
        k=k/10
        ans=ans+arr[i+1]*k
    return ans

def sqrt(inp):
    k=[1]
    while len(k)<100:
        n=num(k)
        if n*n<=inp:
            


'''
for i in range(2,3):
    a=1
    for j in xrange(200):
        a=(a+(i/(a*1.0)))/(2.0)
    k=1
    sum=0
    for j in xrange(100):
        k=k*10
        sum=sum+int(k*a/1)%10
    print sum
'''

