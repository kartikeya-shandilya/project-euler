
from collections import defaultdict
from itertools import combinations as combos

class ulam_seq(object):
    def __init__(self, a, b, info):
        self.a = a
        self.b = b
        self.seq = [self.a, self.b]
        self.N, self.D = info

    def use_period(self, n):
        min_n = (self.b+1)/2-1
        rem = (n-min_n) % self.N
        quot = (n-min_n) / self.N
        new_n = min_n+rem-2
        return new_n, quot

    def nth(self, n):
        self.seq = [self.a, self.b]
        n, quot = self.use_period(n)
        ans = self.fast_next(n)
        ans = quot*self.D + ans
        return ans

    def next(self, n=1):
        while n:
            res = defaultdict(int)
            for i, j in combos(self.seq, 2):
                res[i + j] += 1
            ans = min([k for k in res.keys() if res[k] == 1 and k > max(self.seq)])
            self.seq.append(ans)
            n -= 1
        return ans

    def fast_next(self, n=1):
        while n:
            test = self.seq[-1]
            while True:
                if test>(2*self.b+4):
                    test += 2
                else:
                    test += 1
                cnt = 0
                for elm in self.seq:
                    if test - elm <= elm:
                        break
                    if test - elm in self.seq:
                        cnt += 1
                    if cnt > 2:
                        break
                if cnt == 1:
                    ans = test
                    break
            self.seq.append(ans)
            n -= 1
        return ans



class smart_ulam_seq(object):
    def __init__(self, a, b, info):
        self.a = a
        self.b = b
        self.seq = {self.a, self.b}
        self.N, self.D = info
        self.prev = self.b

    def use_period(self, n):
        min_n = (self.b+7)/2
        if n > min_n:
            rem = (n-min_n) % self.N
            quot = (n-min_n) / self.N
            new_n = min_n+rem-2
        else:
            new_n = n-2
            quot = 0
        return new_n, quot

    def nth(self, n):
        self.seq = {self.a, self.b}
        self.prev = self.b
        n, quot = self.use_period(n)
        ans = self.fast_next(n)
        ans = quot*self.D + ans
        return ans

    def fast_next(self, n=1):
        while n and self.prev < 2*self.b+3:
            if self.prev < 2*self.b+1:
                ans = self.prev + 2
            elif self.prev in (2*self.b+1, 2*self.b+2):
                ans = self.prev + 1
            self.seq.add(ans)
            self.prev = ans
            n -= 1
        test = self.prev
        while n:
            test += 2
            cnt = 0
            if test - 2 in self.seq:
                cnt += 1
            if test - (2*self.b+2) in self.seq:
                cnt += 1
            if cnt == 1:
                ans = test
                self.seq.add(ans)
                self.prev = ans
                n -= 1
        return ans

# period info from
# http://ac.els-cdn.com/009731659290042S/1-s2.0-009731659290042S-main.pdf?_tid=1269308e-e32d-11e5-ab68-00000aacb360&acdnat=1457222022_52f925781e5779f6a26891c2a87a1bc5
info = {5: [32, 126],
        7: [26, 126],
        9: [444, 1778],
        11: [1628, 6510],
        13: [5906, 23622],
        15: [80, 510],
        17: [126960, 507842],
        19: [380882, 1523526],
        21: [2097152, 8388606]}

## testing the function
"""
i = 5
seqa = ulam_seq(2, i, info[i])
seqb = smart_ulam_seq(2, i, info[i])
for j in xrange(3, 1000):
    print j, seqb.nth(j)
"""

#"""
res = 0
for n in xrange(2, 11):
    print "ulam sequence:: %s, %s" % (2, 2*n+1)
    seq = smart_ulam_seq(2, 2*n+1, info[2*n+1])
    res += seq.nth(10**11)
    print res
#"""
# n=2, period = 32, start = 32
# n=3, period = 26, start = 26
# n=4, period = 26, start = 26
