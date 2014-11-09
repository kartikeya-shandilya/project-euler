
# http://www.alpertron.com.ar/QUAD.HTM

init=[(0,-1),(0,1),(-3,-2),(-3,2),(-4,-5),(-4,5),(2,-7),(2,7)]

def X(x,y): return -9*x-4*y-14
def Y(x,y): return -20*x-9*y-28

# when x>0
# r=[(1+x)+-y]/x

listA=[]

for i,j in init:
    x,y=i,j
    for k in xrange(200):
        x,y=X(x,y),Y(x,y)
        if x>0:
            if x not in listA:
                listA.append(x)
            #print "A is:", x, "x: ", 1+x+y,"/",x

print sum(sorted(listA)[:30])
