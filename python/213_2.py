
def jump(i,j):
    deg=4
    if i in (0,29): deg-=1
    if j in (0,29): deg-=1
    return 1.0/deg

stochMat=[]
for i in xrange(900):
    stochMat.append([0.0]*900)

for i in xrange(30):
    for j in xrange(30):
        frm=i+30*j
        prb=jump(i,j)
        if i>0: stochMat[frm][i-1+30*j]=prb
        if i<29: stochMat[frm][i+1+30*j]=prb
        if j>0: stochMat[frm][i+30*(j-1)]=prb
        if j<29: stochMat[frm][i+30*(j+1)]=prb

f=open("213_matrix.txt","w")

for i in xrange(900):
    f.write(','.join([str(x) for x in stochMat[i]])+';\\\n')
