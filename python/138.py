
# http://www.alpertron.com.ar/QUAD.HTM

def X1(x,y): return -9*x-8*y-8
def Y1(x,y): return -10*x-9*y-8

def X2(x,y): return -9*x-8*y+8
def Y2(x,y): return -10*x-9*y+8

listY=[]

x,y=0,-1
for k in xrange(20):
    x,y=X1(x,y),Y1(x,y)
    if y>0: listY.append(y)

x,y=0,1
for k in xrange(20):
    x,y=X2(x,y),Y2(x,y)
    if y>0: listY.append(y)

print sum(sorted(listY)[:13])-1

