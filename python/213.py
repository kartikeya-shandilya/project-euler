
from random import randint

def jump(cell):
    i,j=cell; deg=4
    if i in (0,29): deg-=1
    if j in (0,29): deg-=1
    rnd=randint(1,deg)
    ret=(-1,-1)
    if deg==4:
        if rnd==1: ret=(i+1,j)
        if rnd==2: ret=(i,j+1)
        if rnd==3: ret=(i-1,j)
        if rnd==4: ret=(i,j-1)
    elif i in xrange(1,29) and deg==3:
        if rnd==1: ret=(i+1,j)
        if rnd==2: ret=(i-1,j)
        if rnd==3:
            if j==0:  ret=(i,j+1)
            if j==29: ret=(i,j-1)
    elif j in xrange(1,29) and deg==3:
        if rnd==1: ret=(i,j+1)
        if rnd==2: ret=(i,j-1)
        if rnd==3:
            if i==0:  ret=(i+1,j)
            if i==29: ret=(i-1,j)
    elif deg==2:
        if rnd==1:
            if i==0: ret=(i+1,j)
            else:    ret=(i-1,j)
        else:
            if j==0: ret=(i,j+1)
            else:    ret=(i,j-1)
    #print cell, deg, rnd, ret
    return ret

def vacant():
    sm=0
    for i in xrange(30):
        for j in xrange(30):
            sm+=((i,j) in grid.values())
    return 900-sm

def clear():
    fresh={}
    for i in xrange(30):
        for j in xrange(30):
            fresh[(i,j)]=(i,j)
    return fresh

avg=0.0
for iters in xrange(50):
    grid=clear()
    for times in xrange(50):
        for flea in grid:
            grid[flea]=jump(flea)
    avg+=vacant()
    print iters+1, vacant(), avg/(iters+1)
