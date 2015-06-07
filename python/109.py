
from pprint import pprint
from itertools import combinations_with_replacement, chain, permutations

all_opt = []
for i in ['S','D','T']:
  for j in xrange(1,20+1):
    all_opt += [i+`j`]
all_opt.append('S25')
all_opt.append('D25')

def evl(x):
  if x[0]=='S': return int(x[1:])
  elif x[0]=='D': return 2*int(x[1:])
  else: return 3*int(x[1:])


all_subsets = list(chain.from_iterable(combinations_with_replacement(all_opt,i) for i in range(1,4)))
all_subs = {}

for subs in all_subsets:
  ans = 0
  for char in subs:
    ans += evl(char)
  if ans in all_subs:
    if subs not in all_subs[ans]:
      all_subs[ans].append(subs)
  else:
    all_subs[ans] = [subs]
  #print subs, ans

def getValids(all_subsets):
  valids = []
  chklist = []
  for subs in all_subsets:
    perms = permutations(subs)
    for chk in perms:
      tmp = list(chk[:-1])
      tmp.sort()
      if chk[-1][0] == 'D' and chk not in valids and tmp not in chklist:
        valids.append(chk)
        chklist.append(tmp)
  return valids

ans = 0
for i in xrange(1,100):
  ans += len(getValids(all_subs[i]))

print ans
