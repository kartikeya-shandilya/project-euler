
# http://www.alpertron.com.ar/QUAD.HTM

init=[(0,-1),(0,1),(-1,-2),(-1,2),(2,-5)]

def X(x,y): return -9*x-4*y-2
def Y(x,y): return -20*x-9*y-4

# when x>0
# r=[(1+x)+-y]/x

listA=[]

for i,j in init:
    x,y=i,j
    for k in xrange(100):
        x,y=X(x,y),Y(x,y)
        if x>0:
            if x not in listA:
                listA.append(x)
            #print "A is:", x, "x: ", 1+x+y,"/",x

sorted(listA)[:14]
