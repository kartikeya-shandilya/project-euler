
from math import sqrt

def isPrime (n):
        for i in xrange(2,int(sqrt(n))+1):
                if not n%i:
                        return 0
        return 1

"""
for i in xrange(10**5,2*10**5-1):
        if isPrime(i):
                prSum = 0
                for j in xrange(10):
                        prSum += isPrime(int(`i`.replace('1',`j`)))
                if prSum >= 7:
                        print i,prSum
"""

for num in [141619  ,121313  ,111857]:
        prSum = 0
        numArr = []
        for j in xrange(10):
                numArr.append(int(`num`.replace('1',`j`)))
                prSum += isPrime(int(`num`.replace('1',`j`)))
                print num, numArr[-1], prSum
        print

