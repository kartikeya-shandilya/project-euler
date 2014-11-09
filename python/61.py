
def polyNumb(i,d):
    arr=[]
    n=0
    while 1:
        n=n+1
        if   i==3:  num=n*(n+1)/2
        elif i==4:  num=n*n
        elif i==5:  num=n*(3*n-1)/2
        elif i==6:  num=n*(2*n-1)
        elif i==7:  num=n*(5*n-3)/2
        elif i==8:  num=n*(3*n-2)
        if len(`num`)==d:   arr.append(num)
        if len(`num`)>d:    break
    return arr

bigDict={}
for i in xrange(3,8+1):
    bigDict[i]=polyNumb(i,4)

def verify(done,n,st,sm):
    d=len(done)
    if d==6 and n%100==st/100:   print "ans", sm
    ind=[i for i in range(3,9) if i not in done]
    elig=[]
    for k in ind:
        elig+=[i for i in bigDict[k] if i/100==n%100]
    if len(elig)==0:    return
    for j in elig:
        for k in ind:
            if j in bigDict[k]: dd=[k]
        verify(done+dd,j,st,sm+j)
    return

for i in bigDict[3]:
    verify([3],i,i,i)

