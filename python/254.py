
factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def f(n):
  return sum([factorial[int(x)] for x in `n`])

global g
g = {}

def sf(n):
  global g
  ans = sum([int(x) for x in `f(n)`])
  if ans not in g and ans<=150:
    g[ans] = n
  return ans

for i in xrange(1,5000000):
  sf(i)

def sg(n):
  return sum([int(x) for x in `g[n]`])

tot = 0
for i in xrange(1,150+1):
  tot = tot + sg(i)
  print i, g[i], sg(i), tot

