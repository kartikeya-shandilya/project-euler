x=[1]*2000
for j in xrange(2000):
    for i in xrange(2000):
        if i < 1999:
            x[i] = x[i] + x[i+1]
        else:
            x[i] = x[0] + x[i]
        if (2000*j + i) % 1000 == 0:
            print 2000*j + i, ":", x[i]%2009
