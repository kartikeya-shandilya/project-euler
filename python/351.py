
dots=[(1,2),(0,4),(1,6)]
cnt=len(dots)+1

start=[(1,6)]
n=6;

def gcd(a,b):
    while 1:
        if b>a: c=a; a=b; b=c
        if b==0:    return 0
        if a%b==0:  return b
        else:       a=a-b

for i in xrange(n-2):
    new_start=[]
    for j in xrange(len(start)):
        if j==0 and start[0][0]!=0:
            new_start.append((0,start[0][1]+2))
        new_start.append((start[j][0]+1,start[j][1]+2))
        gcd_elm=gcd(start[j][0],start[j][1])
        if gcd_elm:
            elm_std=(start[j][0]/gcd_elm,start[j][1]/gcd_elm)
        if elm_std not in dots and gcd_elm!=0:
            dots.append(elm_std)
            cnt+=2
    start=new_start

print 3*n*(n+1)-6*cnt
