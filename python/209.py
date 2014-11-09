
bdict={}
cycle=[]

for i in xrange(64):
    j=bin(i)[2:]
    j='0'*(6-len(j))+j
    a,b,c=j[:3]
    k=j[1:]+`int(a)^(int(b)&int(c))`
    l=0
    for d in k: l=l*2+int(d)
    bdict[i]=l

loops=[1]*64

for i in xrange(64):
    j=len(cycle)
    if loops[i]:
        cycle.append([])
    k=i
    while loops[k]:
        cycle[j].append(k)
        loops[k]=0
        k=bdict[k]

    
# consec(n)={F=[1,1;1,0];ans=(F^(n+1))[1,1]-1*(F^(n-3))[1,1]}
# lst=[1,2,3,6,6,46]; prod(i=1,#lst,consec(lst[i]))
# 15964587728784
