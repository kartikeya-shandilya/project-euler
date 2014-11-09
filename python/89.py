
rToA = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def romanToArabic(r):
    for i in xrange(len(r)-1):
        a = 0
        if(rToA[r[i+1]]<=rToA[r[i]]):
            a += rToA[r[i]]
        else:
            a += (rToA[r[i+1]]-rToA[r[i]])
            i += 1
    if i!=len(r)-1:
        a += rToA[r[i]]
    return a

