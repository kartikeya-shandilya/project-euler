def isElig(n):
    N=str(n)
    f1=reduce(lambda x,y: int(x)*int(y), N)!=0
    f2 =(N[0]!=N[1]) * (N[1]!=N[2]) * (N[2]!=N[3])
    f2*=(N[0]!=N[2]) * (N[1]!=N[3])
    f2*=(N[0]!=N[3])
    return f1*f2

def maxInt(arr):
    maxInt=0
    for i in xrange(1,int(max(arr))):
        if i not in arr:
            break
    return i-1  

allN={}
for n in xrange(10**3, 10**4):
    if not isElig(n):
        continue
    rng=[]
    for s1 in ['+','-','*','/']:
        for s2 in ['+','-','*','/']:
            for s3 in ['+','-','*','/']:
                N=str(n)
                exp='(((('+N[0]+'*1.0)'+s1+'('+N[1]+'*1.0))'+s2+'('+N[2]+'*1.0))'+s3+'('+N[3]+'*1.0))'
                ans=eval(exp)
                if ans>0 and ans==int(ans):
                    rng.append(int(ans))
    N=str(n)
    srtN=reduce(lambda x,y: x+y, sorted([N[0],N[1],N[2],N[3]]))
    if srtN not in allN:
        allN[srtN]=[]
    allN[srtN]+=rng

mxm=0
bst=[]
for i in allN:
    chl=maxInt(allN[i])
    if chl>=35:
        print i, chl, '\n\t', sorted(set(allN[i]))
    if chl>mxm: mxm=chl; bst=i
