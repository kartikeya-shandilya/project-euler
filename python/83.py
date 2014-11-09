
File=open("matrix.txt")
dist=[]
for line in File.readlines():
    dist.append(line.strip().split(','))

temp={}; uvis=[]

for i in xrange(len(dist)):
    for j in xrange(len(dist)):
        dist[i][j]=eval(dist[i][j])
        temp[(i,j)]=999999
        uvis.append((i,j))

def getNbrs(node):
    i,j=node; nbrs=[]
    if i>0:             nbrs.append((i-1,j))
    if j>0:             nbrs.append((i,j-1))
    if i+1<len(dist):   nbrs.append((i+1,j))
    if j+1<len(dist):   nbrs.append((i,j+1))
    return nbrs

def getMin():
    minN=(0,0); minD=999999999
    for node in uvis:
        if temp[node]<minD:
            minN=node; minD=temp[node]
    return minN,minD

node=(0,0); temp[node]=dist[0][0]

while uvis!=[]:
    nbrs=getNbrs(node)
    for nbr in nbrs:
        if nbr in uvis:
            i,j=nbr
            temp[nbr]=min(temp[nbr],temp[node]+dist[i][j])
    uvis.remove(node)
    node,minD=getMin()
    
print temp[(len(dist)-1,len(dist)-1)]
