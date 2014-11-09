
def getIndex(face):
    ind=0
    mul=1
    for i in xrange(3):
        for j in xrange(3):
            ind += mul*(face[2-i][2-j]!=0)
            mul *= 2
    return ind

def getBinary(x):
    ans=[]
    while x:
        ans.append(x%2)
        x/=2
    if ans==[]:
        ans=[0]
    return ans[::-1]

def getFace(x):
    bin = getBinary(x)
    face = clean[:]
    for j in xrange(len(bin)):
        face[8-j]=bin[::-1][j]
    face = [face[0:3], face[3:6], face[6:9]]
    return face

clean=[0,0,0,0,0,0,0,0,0]

def getCopy(cuboid):
    newCuboid=[]
    for plane in cuboid:
        newplane=[]
        for row in plane:
            newplane.append(row[:])
        newCuboid.append(newplane)
    return newCuboid

def nextIJ(i,j):
    if i==2:
        return 0, j+1
    else:
        return i+1, j

def fillWays(cuboid,i,j,k):
    origCuboid=getCopy(cuboid)
    if j==3:
        ind=getIndex(origCuboid[1])
        result[ind]+=1
        return
    if origCuboid[0][i][j]!=0:
        if i<2:        fillWays(origCuboid,i+1,j,k)
        elif j<2:    fillWays(origCuboid,0,j+1,k)
        else:
            ind=getIndex(origCuboid[1])
            result[ind]+=1
            return            
    else:
        if i<2:
            cuboid=getCopy(origCuboid)
            cuboid[0][i][j]=k
            if not cuboid[0][i+1][j]:
                cuboid[0][i+1][j]=k
                x, y = nextIJ(i, j); fillWays(cuboid,x,y,k+1)
        if j<2:
            cuboid=getCopy(origCuboid)
            cuboid[0][i][j]=k
            if not cuboid[0][i][j+1]:
                cuboid[0][i][j+1]=k
                x, y = nextIJ(i, j); fillWays(cuboid,x,y,k+1)
        cuboid=getCopy(origCuboid)
        cuboid[0][i][j]=k; cuboid[1][i][j]=k
        x, y = nextIJ(i, j); fillWays(cuboid,x,y,k+1)

for i in xrange(512):
    start=[getFace(i),[[0]*3]*3]
    result=[0]*512
    fillWays(start,0,0,1)
    print result

