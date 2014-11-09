
import numpy

def poly(a,b):
 c=[]
 for k in xrange(45):
  c.append(0)
 for i in xrange(len(a)):
  for j in xrange(len(b)):
   if i+j<=44: c[i+j]+=a[i]*b[j]
 return c

maxim=0
for i in range(1,20):
	for j in range(i,20):
		for k in range(max(6-(i+j),j+1),max(25-(i+j),1)):
			x=numpy.zeros(45,int)
			y=numpy.zeros(45,int)
			z=numpy.zeros(45,int)
			x[0]=1; x[i]=1;
			mx=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
			for l in xrange(9):
				mx=poly(mx,x)
			y[0]=1; y[j]=1;
			my=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
			for l in xrange(9):
				my=poly(my,y)
			z[0]=1; z[k]=1;
			mz=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
			for l in xrange(9):
				mz=poly(mz,z)
			mul=poly(mx,poly(my,mz))
			print i,j,k,mul[44]
			#if(mul[44]>maxim):
			#	maxim=mul[44]
			#	print i,j,k,x,y,z,mul[44]


