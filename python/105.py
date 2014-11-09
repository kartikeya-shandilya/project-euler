
from itertools import combinations, chain

"""
def getAllSubsets(fullset):
  if len(fullset)==1:
    return [fullset]
  ans = [fullset]
  for i in fullset:
    tmp = fullset[:]
    tmp.remove(i)
    all_subs = getAllSubsets(tmp)
    for subs in all_subs:
      if subs not in ans:
        ans.append(subs)
  return ans
"""

def getAllSubsets(fullset):
  return list(chain.from_iterable(combinations(fullset, i) for i in xrange(2,len(fullset))))


def giveOK(fullset):
  all_subs = getAllSubsets(fullset)
  ans = []
  flag = True
  for i in xrange(2,len(fullset)):
    flag *= (sum(fullset[:i]) > sum(fullset[1-i:]))
  if not flag:
    return flag
  for subs in all_subs:
    tmp = sum(subs)
    if tmp in ans:
      return False
    else:
      ans.append(tmp)
  return True

data = open('sets.txt','r')
ans = 0
for line in data.readlines():
  row = [int(x) for x in line.strip().split(',')]
  row.sort()
  ans += giveOK(row) * sum(row)

print ans



