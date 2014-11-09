
from pprint import pprint
from math import sqrt, floor
#from bisect import bisect_left

upto = 25000
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

global knownFactorizations
knownFactorizations = {}
knownFactorizations[1] = None

def getFactorizations(n):
  global knownFactorizations
  if n in knownFactorizations:
    return knownFactorizations[n]
  divs = getDivisors(n)
  ans = [[divs[-1]]]
  for div in divs[1:-1]:
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

minProdSum = {}
ksCovered = []
ansList = []
stop = 20000

for i in xrange(2,2*stop+1):
  if len(ksCovered)>=(stop-1):
    break
  allFaczs = getFactorizations(i)
  for faczn in allFaczs:
    tot = sum(faczn)
    if tot <= i:
      k = len(faczn) + i - tot
      if k not in minProdSum:
        minProdSum[k] = [i, [1]*(i-tot)+faczn]
        if k>1 and k<=stop:
          ksCovered.append(k)
          if i not in ansList:
            ansList.append(i)

#print minProdSum
#print ksCovered
#print ansList
print sum(ansList)

"""
ansList = []
for i in xrange(2,12000+1):
  if i not in minProdSum:
    print i, "not found"
  j = minProdSum[i][0]
  if j not in ansList:
    ansList.append(j)

print sum(ansList)
"""

"""
def divInRange(n,k,l):
  divs = getDivisors(n)
  ans  = []
  for div in divs:
    if div<k:
      continue
    elif div>=k and div<=l:
      ans.append(div)
    else:
      break
  return ans

def divInRange(n,k,l):
  divs = getDivisors(n)
  frm = bisect_left(divs, k)
  to = bisect_left(divs, floor(l))
  return divs[frm:to+1]
"""

"""
def getBreaks(k,n):
  choices = []
  while k > 0:
    if not len(choices):
      for div in divInRange(n, 1, n**(1.0/k)):
        choices.append([[div],n/div])
    else:
      new = []
      for choice in choices:
        seq, num = choice
        if k > 1:
          divs = divInRange(num, seq[-1], num**(1.0/k))
        else:
          divs = []
          if num>=seq[-1]:  divs=[num]
        for div in divs:
          tmp = seq[:] 
          tmp.append(div)
          new.append([tmp, num/div])
      choices = new
    k -= 1
  return choices

def goodOnes(k,n):
  choices = getBreaks(k,n)
  for choice in choices:
    if sum(choice[0])==n:
      return choice[0]
  return None

minprodsum = []
for k in xrange(2,1000+1):
  if not k%100:
    print k
  if k>2 and flag==0:
    print "not found any:",k-1
    break
  flag = 0
  for n in xrange(k,5*k):
    result = goodOnes(k,n)
    if result:
      flag = 1
      #print k, n
      if n not in minprodsum:
        minprodsum.append(n)
      break

print sum(minprodsum)
"""

