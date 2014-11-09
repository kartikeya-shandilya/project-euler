
pro=1
for i in range(2,10):
 pro*=i

def sum(i):
 j=str(i)
 l=0
 for k in xrange(len(j)):
  l=l+int(j[k])
 return l

def prod(i):
 j=str(i)
 l=1
 for k in xrange(len(j)):
  l=l*int(j[k])
 return l

print sum(192384576)
print prod(192384576)

max=0
for i in  range(1,100000):
 k=""
 for j in range(1,10):
  if len(str(i*j))+len(k)<=9:
   k=k+str(i*j)
  else:
   break
 if int(k)>max and sum(int(k))==45 and prod(int(k))==pro:
  max=int(k)
  temp=i

print max,temp

