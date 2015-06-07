
from pprint import pprint
from math import sqrt, floor
#from bisect import bisect_left

upto = 1000000
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

# gives just the list of primes that divide n
def getFactors(n):
  global primes
  factors = []
  i = 0
  while n>1 and primes[i]<=n:
    if isPrime[n-1]:
      factors.append(n)
      break
    elif not n%primes[i]:
      factors.append(primes[i])
      while not n%primes[i]:
        n = n/primes[i]
      i = 0
    else:   i += 1
  return factors

# gives square free divisors
def getDivisors(n):
  factors = getFactors(n)
  divisors = [1]
  for i in factors:
    new = []
    for k in divisors:
      new.append(i*k)
    divisors += new
  return sorted(divisors)

# gives square free factorizations
global knownFactorizations
knownFactorizations = {}
knownFactorizations[1] = None

def getFactorizations(n):
  if n in knownFactorizations:
    return knownFactorizations[n]
  divs = getDivisors(n)
  ans = []
  if n==divs[-1]:
    ans = [[divs[-1]]]
  for div in divs[1:]:
    if div>sqrt(n):
      break
    rest = getFactorizations(n/div)
    if not rest:
      continue
    for faczn in rest:
      if faczn[0] < div:
        continue
      tmp = faczn[:]
      tmp = [div] + tmp
      ans.append(tmp)
  knownFactorizations[n] = ans
  return ans

ans = 0
for i in xrange(2,1000000+1):
  ans += len(getFactorizations(i))

print ans

