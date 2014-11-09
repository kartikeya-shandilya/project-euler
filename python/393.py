
allPos = ['v1','v2','h1','h2','a1','a2','b1','b2','c1','c2','d1','d2']

rIndep = ['v1','v2','a1','a2','b1','b2']
dIndep = ['h1','h2','b1','b2','c1','c2']
lIndep = ['v1','v2','c1','c2','d1','d2']
uIndep = ['h1','h2','a1','a2','d1','d2']

vRight = {
    '':rIndep,
    'v1':rIndep, 'v2':rIndep,
    'h1':['h1','c1','d2'], 'h2':['h2','c2','d1'],
    'a1':['h2','c2','d1'], 'a2':['h1','c1','d2'],
    'b1':['h1','c1','d2'], 'b2':['h2','c2','d1'],
    'c1':rIndep, 'c2':rIndep,
    'd1':rIndep, 'd2':rIndep
}

vDown = {
    '':dIndep,
    'v1':['v1','a1','d2'], 'v2':['v2','a2','d1'],
    'h1':dIndep, 'h2':dIndep,
    'a1':dIndep, 'a2':dIndep,
    'b1':['v1','a1','d2'], 'b2':['v2','a2','d1'],
    'c1':['v2','a2','d1'], 'c2':['v1','a1','d2'],
    'd1':dIndep, 'd2':dIndep
}

def countAll(n,x,y,matrix):
    global count
    vL = vU = val = set(allPos)
    vD = set(dIndep); vR = set(rIndep);
    if x!=0:   vD=set(vDown[matrix[x-1][y]])
    if y!=0:   vR=set(vRight[matrix[x][y-1]])
    if x==n-1: vU=set(uIndep)
    if y==n-1: vL=set(lIndep)
    val = val.intersection(vD)
    val = val.intersection(vR)
    val = val.intersection(vL)
    val = val.intersection(vU)
    #if (x+y)%2==0 and (x+y not in [0,n,2*n]): val = val.difference(set(['a1','a2','c1','c2']))
    #print x,y,val
    for chk in val:
        matrix[x][y] = chk
        if   x<n-1: countAll(n,x+1,y,matrix)
        elif y<n-1: countAll(n,0,y+1,matrix)
        else:
            #print matrix
            count = count+1

matrix=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
global count
count = 0
countAll(6,0,0,matrix)
print "Total Count =", count
