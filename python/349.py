
blck=[]; i=j=0; d=0; cnt=0; loop=0;
while 1:
    if (i,j) in blck:
        blck.remove((i,j))
        d=(d+1)%4
        if   d==0:    i+=1
        elif d==1:    j+=1
        elif d==2:    i-=1
        elif d==3:    j-=1
    else:
        blck.append((i,j))
        d=(d-1)%4
        if   d==0:    i+=1
        elif d==1:    j+=1
        elif d==2:    i-=1
        elif d==3:    j-=1
    cnt+=1
    if cnt>=10647 and (cnt-10647)%104==0:
        loop+=1
        print cnt, loop, i, j, (i,j) in blck, d, len(blck)
    if loop==50: break
