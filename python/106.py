
def getSubsets(subset, l):
        #print subset, l
        ans = []
        if len(subset) == l:
                return [subset]
        for i in subset:
                tmp = subset[:]
                tmp.remove(i)
                all_subs = getSubsets(tmp, l)
                for subs in all_subs:
                        if subs not in ans:
                                ans.append(subs)
        return ans


def magnitude(a, b):
        ans1 = 1
        ans2 = 1
        for i in xrange(len(a)):
                ans1 *= (a[i]>=b[i])
                ans2 *= (a[i]<b[i])
        return 1 - ans1 - ans2


def checksReq(subset, l):
        all_subs = getSubsets(subset, l)
        #print subset, all_subs
        ans = 0
        for a in all_subs:
                tmp = subset[:]
                for i in a:
                        tmp.remove(i)
                new_subs = getSubsets(tmp, l)
                for b in new_subs:
                        #print a, b, magnitude(a,b)
                        ans += magnitude(a, b)
        #print subset, l, ans
        return ans/2


def allChecks(subset):
        ans = 0
        for i in xrange(2,1+len(subset)/2):
                ans += checksReq(subset, i)
        return ans


tmp = range(1,13)
print allChecks(tmp)

