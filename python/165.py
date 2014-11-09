
sN=290797
def sNew(sN):
    return (sN*sN)%50515093

def slope(seg):
    x1, y1, x2, y2 = seg
    if x1==x2: return "Inf"
    return (y2 - y1)*1.0/(x2 - x1)

segs=[]
slps=[]
for cnt in xrange(5000):
    seg=[]
    for i in xrange(4):
        sN=sNew(sN)
        seg.append(sN%500)
    segs.append(seg)
    slps.append(slope(seg))

tolr=0.0000000001
def inSide(seg, pt):
    x1, y1, x2, y2 = seg
    x3, y3 = pt
    chk = (x3<max(x1,x2)-tolr and x3>min(x1,x2)+tolr)
    print seg, pt, chk
    return chk

def iSect(i,j):
    # (x1, y1) to (x2, y2) and (p1, q1) to (p2, q2)
    x1, y1, x2, y2 = segs[i]
    p1, q1, p2, q2 = segs[j]
    slp1 = slps[i]
    slp2 = slps[j]
    if slp1==slp2: return 0
    if slp1=="Inf":   x12 = x1
    elif slp2=="Inf": x12 = p1
    else:             x12 = (slp2*p1 + y1 - slp1*x1 - q1)*1.0/(slp2 - slp1)
    if slp1!="Inf":   y12 = y1 + slp1 * (x12 - x1)
    else:             y12 = q1 + slp2 * (x12 - p1)
    pt = [x12, y12]
    if inSide(segs[i], pt) and inSide(segs[j], pt):
        return 1
    return 0

valInt=0
for i in xrange(5000):
    for j in xrange(i+1,5000):
        valInt += iSect(i,j)
print valInt

