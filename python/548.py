
import sys
sys.setrecursionlimit(2000)

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


def isvalid(combo, nmax=10**9):
    num = 1
    for i, n in enumerate(combo):
        num = num * prime[i]**n
    return num<nmax, num


def firstidx(combo):
    idx = 0
    for i in xrange(len(combo)-1, 0, -1):
        if combo[i] < combo[i-1]:
            idx = i
            break
    combo[idx] += 1
    newcombo = combo[:idx+1] + [1]*len(combo[idx+1:])
    return idx, newcombo


def newidx(combo, nmax=10**9):
    newcombo = [1]*(len(combo)+1)
    return len(combo), newcombo


def find(combo, nmax=10**9):
    idx, newcombo = firstidx(combo)
    res = isvalid(newcombo, nmax)
    if res[0]:
        print res[1]
        find(newcombo, nmax)
    else:
        idx, newcombo = newidx(combo, nmax)
        res = isvalid(newcombo, nmax)
        if res[0]:
            print res[1]
            find(newcombo, nmax)


find([1], 10**5)
