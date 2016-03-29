
import pyprimesieve as pp
from collections import defaultdict

primelst = pp.primes(10**7)
myprimes = set(primelst)
def isprime(n):
    return n in myprimes


def changedigit(n):
    str_n = str(n)
    edges = defaultdict(set)
    for i, dig in enumerate(str_n):
        alldigs = [str(x) for x in range(10) if str(x) != dig]
        if i == 0:
            alldigs.pop(0)
        for newdig in alldigs:
            testprime = str_n[:i] + newdig + str_n[i+1:]
            testprime = int(testprime)
            if isprime(testprime):
                edges[testprime].add(n)
    return edges


def adddigit(n):
    str_n = str(n)
    edges = defaultdict(set)
    alldigs = [str(x) for x in range(1, 10)]
    for newdig in alldigs:
        testprime = newdig + str_n
        testprime = int(testprime)
        if isprime(testprime):
            edges[testprime].add(n)
    return edges


def join_dictsets(dset1, dset2):
    allkeys = set(dset1).union(dset2)
    result = defaultdict(set)
    for key in allkeys:
        result[key] = dset1[key].union(dset2[key])
    return result


def relatives(rels):
    newrels = defaultdict(set)
    result = defaultdict(set)
    for rel in rels:
        new_ad = adddigit(rel)
        newrels = join_dictsets(newrels, new_ad)
    result.update(newrels)
    rels = newrels.copy()
    n = len(str(list(rels)[0]))
    newrels = defaultdict(set)
    while n:
        for rel in rels:
            new_ch = changedigit(rel)
            newrels = join_dictsets(newrels, new_ch)
        rels = newrels.copy()
        n -= 1
    result = join_dictsets(result, newrels)
    return result


connectcache = {}
def isconnected(p, rels, maxelm, done=set()):
    if p not in rels:
        return False
    else:
        if 3 in rels[p] or 7 in rels[p]:
            connectcache[p] = True
            return connectcache[p]
        for elm in rels[p]:
            if elm < maxelm and elm not in done:
                tmp = done.copy()
                tmp.add(elm)
                flag = isconnected(elm, rels, maxelm, tmp)
                if flag:
                    connectcache[p] = True
                    return connectcache[p]
        connectcache[p] = False
        return connectcache[p]


rels = {3: {2}, 7: {2}}
allrels = {}
for i in xrange(2, 5+1):
    rels = relatives(rels)
    allrels.update(rels)


ans = 0
for key in allrels:
    if not isconnected(key, allrels, key):
        ans += key
print ans
