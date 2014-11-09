
p1=[2,3,4]
p2=[1,5]

def game(p):
    q=[]
    for i in p:
        for j in p:
            if i+j+2 not in q:
                print i+j+2,"=", i,"+ 2 +",j
                q.append(i+j+2)
    return q

def playme(p1,p2):
    p1_new1=game(p1)
    p1_new2=game(p2)
    for i in p1_new1:
        if i not in p1:
            p1.append(i)
    for j in p1_new2:
        if j not in p1:
            p1.append(j)
    mx=max(max(p1),max(p2))
    for i in xrange(1,mx):
        if i not in p1 and i not in p2:
            p2.append(i)
    return p1,p2

while 1:
    p1,p2=playme(p1,p2)
    if max(max(p1),max(p2)) > 20:
        break

print p1,p2
