
x = [0,0,0,0,0]

def bin2dec(x):
    return x[0]*16 + x[1]*8 + x[2]*4 + x[3]*2 + x[4]

done = [0]
temp = [0,0,0,0,0]

for i in xrange(1,32):
    for j in xrange(4):
        temp[j] = x[(i+j)%32]
    temp[4] = 0
    if bin2dec(temp) in done:
        temp[4] = 1
    elif bin2dec(temp) in done:
        break
    x.append(temp[4])
    done.append(bin2dec(temp))
    print done

print x
print len(x)
print len(done)
