
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

def giveOK(fullset):
  all_subs = getAllSubsets(fullset)
  ans = []
  flag = 1
  for i in xrange(2,len(fullset)):
    flag *= sum(fullset[:i]) > sum(fullset[1-i:])
  if not flag:
    return flag
  for subs in all_subs:
    tmp = sum(subs)
    if tmp in ans:
      return False
    else:
      ans.append(tmp)
  return True

global best
#best = [11, 17, 20, 22, 23, 24]
best = [20, 20+11, 20+17, 20+20, 20+22, 20+23, 20+24]

def findSubset(n, subset=[]):
  global best
  if n==0:
    if sum(best)>sum(subset):
      best = subset
      print best, sum(best)
  elif not subset:
    for i in xrange(best[len(best)-n]-1,best[len(best)-n]+1+1):
      findSubset(n-1, [i])
  else:
    for i in xrange(subset[-1]+1,best[len(best)-n]+len(best)+1):
      tmp = subset[:]
      tmp.append(i)
      if giveOK(tmp):
        findSubset(n-1, tmp)

findSubset(7)

"""
def nextElem(arr, done, n, sol):
        if not n:
                if sum(arr)<sum(sol[-1]):
                        sol.append(arr)
                return
        ll=max(arr[-1],arr[-1]-arr[0])+1
        ul=min(sum(arr[-2:])-arr[0]+2,sum(arr[:2]))
        if ll>=ul: return
        poss=[elm for elm in xrange(ll,ul) if elm not in done]
        print arr, ll, ul
        print done
        print new
        for st in poss:
                new=[st+elm for elm in arr]
                if len(set(done+new))==len(done)+len(new):
                        ans=nextElem(arr+[st], done+new, n-1, sol)
        return

sol=[[1000]]
x=1000
for a in xrange(11,12):
        for b in xrange(a+5,a+6):
                ans=nextElem([a,b], [a,b,a+b], 4, sol)
                if sum(sol[-1])<x:
                        x=sum(sol[-1])
                        print sol[-1],x 
"""

