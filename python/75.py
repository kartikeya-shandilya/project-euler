
from math import sqrt, ceil, floor

valid=[]

mx = 150
ans = 0
for k in xrange(3, mx/2):
    ct=0
    for l in xrange(1, int(floor(sqrt(sqrt(k))))):
        if k%(l*l): continue
        ll = int(floor(sqrt(k/l/l/2.0)))+1
        ul = int(ceil(sqrt(k/l/l)))+1
        for ch in xrange(ll, ul):
            if (k/l/l)%ch==0:
                if (k/l/l)/ch>ch and (k/l/l)/ch<2*ch and (k/l/l)/ch!=ch:
                    ct += 1
                if ct>1: break
        if ct>1: break
    if ct==1:
        valid.append(2*k)
    
print valid
print len(valid)
