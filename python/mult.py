def makeDict(a):
	if type(a)==type(1) or type(a)==type(1L):
		return {0:a}
	else: return a

def plus(a,b):
	#print "plus:", a, b
	result={}
	x=set([i for i in a]).union(set([j for j in b]))
	#print "x is:", x
	for k in x:
		#print "k is:", k
		result[k]=0
		if k in a:
			result[k]+=a[k]
		if k in b:
			result[k]+=b[k]
		#print 'res[k]:', result[k]
	return result

def multiply(a,b,mx):
	#print "a is:", a
	#print "b is:", b
	a=makeDict(a)
	b=makeDict(b)
	result={}
	for i in a:
		#print "i is:", i, "a[i] is:", a[i] 
		for j in b:
			#print "j is:", j, "b[j] is:", b[j]
			if i+j<=mx:
				if (type(a[i])==type(1) or type(a[i])==type(1L)) and (type(b[j])==type(1) or type(b[j])==type(1L)):
					if i+j not in result:
						result[i+j]=a[i]*b[j]
					else:
						result[i+j]+=a[i]*b[j]
				else:
					if i+j not in result:
						result[i+j]=multiply(a[i],b[j],10000)
					else:
						result[i+j]=plus(result[i+j],multiply(a[i],b[j],10000))
				#print "result[i+j]:", result[i+j]
				#print "----"
	#print "============"
	return result


x={0:{1:1}, 1:{0:1,1:-1}}
#print x
#print multiply(x, x)

y={0:1,1:2,2:3}
z={1:-1,2:0,3:1}
#print y,z
#print plus(y,z)


x={0:{1:1}, 1:{0:1,1:-1}}
y={0:{1:2}, 1:{0:1,1:-2}}
print x,y
ans=multiply(x,y,100)
print ans
print "----"

z={0:{1:3}, 1:{0:1,1:-3}}
print ans,z
ans=multiply(ans,z,100)
print ans
print "----"


"""
ans={0:1}
maxCoeff=10
maxMults=3
for i in xrange(1,maxMults+1):
	x={0:{1:i}, 1:{0:1,1:-i}}
	ans=multiply(ans,x,maxCoeff)

print ans
"""

