
import sys
import random

def toBinary(n):
  r = []
  while (n > 0):
    r.append(n % 2)
    n = n / 2
  return r

def test(a, n):
  b = toBinary(n - 1)
  d = 1
  for i in xrange(len(b) - 1, -1, -1):
    x = d
    d = (d * d) % n
    if d == 1 and x != 1 and x != n - 1:
      return True # Complex
    if b[i] == 1:
      d = (d * a) % n
  if d != 1:
    return True # Complex
  return False # Prime

def MillerRabin(n, s = 50):
  if n<10:
    if n in [2,3,5,7]:
      return True
    else: return False
  for j in xrange(1, s + 1):
    a = random.randint(1, n - 1)
    if (test(a, n)):
      return False # n is complex
  return True # n is prime

harsh = [1,2,3,4,5,6,7,8,9]
nHrsh = []
pSrth = []
srth = 0

def digSum(n):
 sm = 0
 while n:
  sm += n%10
  n = n/10
 return sm

def lrHarsh(n):
 global harsh, nHrsh, srth
 if not n: return
 for num in harsh:
  nHrsh.append(10*num)
  for i in xrange(1,10):
   test = 10*num+i
   if MillerRabin(test):
    if MillerRabin(num/digSum(num)):
     srth += test
     pSrth.append(test)
   if not test % digSum(test):
    nHrsh.append(test)
 harsh = nHrsh
 nHrsh = []
 n -= 1
 lrHarsh(n)

lrHarsh(13)
print srth
#print harsh
#print pSrth

