
# create a dict with all numbers as key, their factors as value
# create a list of all factors of all numbers in a given range

primelist=[2,3]

def closeprimes(n):
    closeprimes=[]
    for i in xrange(5,n,6):
        closeprimes.append(i)
        closeprimes.append(i+2)
    return closeprimes

def actualprimes(n):
    global primelist
    for i in closeprimes(n):
        for j in primelist:
            if j*j>i:
                primelist.append(i)
                break
            if i%j==0:
                break

actualprimes(20000000)
#print primelist
print len(primelist)

