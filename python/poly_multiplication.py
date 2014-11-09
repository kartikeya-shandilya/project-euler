

def poly(a,b):
 c=[]
 for k in range(0,len(a)+len(b)-1):
  c.append(0)
 for i in range(0,len(a)):
  for j in range(0,len(b)):
   c[i+j]+=a[i]*b[j]
 return c

a=[1,1,1,1,1,1]
b=[1,1,1,1]

pete=[1]
coli=[1]

for i in range(9):
	pete=poly(pete,b)
for i in range(6):
	coli=poly(coli,a)

print len(pete),"pete"
print pete
print len(coli),"coli"
print coli


pete.insert(0,0)
pete.insert(0,0)
pete.insert(0,0)

sum=0; coeff=0;
for i in range(len(pete)):
	coeff+=pete[i]*sum
	sum+=coli[i]
	print "int",coeff

print coeff
print coeff/(1.0*4**9*6**6)


'''
a=[6,6,3,1]
b=[2,2,1]
x=[1]
for i in range(1,10):
 x=poly(x,a)

x=poly(x,b)

print x
print x[17]

fac=1
for i in range(1,18):
 fac=fac*i

print (x[17]*fac*9)/(2*(6**9))
'''
