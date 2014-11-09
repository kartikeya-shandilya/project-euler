
from pprint import pprint
from math import sqrt, floor
#from bisect import bisect_left

upto = 750000
isPrime = [1]*upto
isPrime[0] = 0
indx = 0
while 1:
  indx += 1
  if indx >= upto:        break
  if not isPrime[indx]:   continue
  step = 2*(indx + 1)
  while step <= upto:
    isPrime[step - 1] = 0
    step += (indx + 1)

global primes
primes = []
indx = 0
while indx < upto:
  if isPrime[indx]:
    primes.append(indx+1)
  indx += 1

global knownDivisors
knownDivisors = {}

def getFactors(n):
  global primes
  factors = {}
  i = 0
  while n>1 and primes[i]<=n:
    if isPrime[n-1]:
      if n not in factors:            factors[n]  = 1
      else:                           factors[n] += 1
      break
    elif not n%primes[i]:
      if primes[i] not in factors:    factors[primes[i]]  = 1
      else:                           factors[primes[i]] += 1
      n = n/primes[i]
      i = 0
    else:   i += 1
  return factors

def getDivisors(n):
  global knownDivisors
  if n in knownDivisors:
    return knownDivisors[n]
  factors = getFactors(n)
  divisors = [1]
  elms    = factors.keys()
  for i in elms:
    new = []
    for j in xrange(1,factors[i]+1):
      for k in divisors:
        new.append(i**j*k)
    divisors += new
  knownDivisors[n] = sorted(divisors)
  return knownDivisors[n]

def gcd(m,n):
  if not m%n: return n
  else:       return gcd(n,m%n)

count = 0
for i in xrange(upto+1):
  divs = getDivisors(i)
  known = []
  for l in divs:
    rDivs = getDivisors(i/l)
    for m in rDivs:
      if m<sqrt(i/l/2.0):
        continue
      if m>sqrt(i/l):
        break
      if gcd(m,i/l/m)==1 and i/l/m>m and 2*m>i/l/m:
        a=l*(m**2-(i/l/m-m)**2)
        b=l*(2*m*(i/l/m-m))
        c=l*(m**2+(i/l/m-m)**2)
        if [min(a,b),max(a,b),c] not in known:
          known.append([min(a,b),max(a,b),c])
  count += (len(known)==1)
  #if len(known):
  #  print 2*i, ":", known

print count


