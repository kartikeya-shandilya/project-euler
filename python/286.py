def makeDict(a):
    if type(a)!=type({}): return {0:a}
    else:                 return a

def plus(a,b):
    result={}
    x=set([i for i in a]).union(set([j for j in b]))
    for k in x:
        result[k]=0
        if k in a: result[k]+=a[k]
        if k in b: result[k]+=b[k]
    return result

def multiply(a,b):
    result={}
    a=makeDict(a)
    b=makeDict(b)
    for i in a:
        for j in b:
	    if type(a[i])!=type({}) and type(b[j])!=type({}):
		try:	result[i+j]+=a[i]*b[j] 
	  	except: result[i+j] =a[i]*b[j]
	    else:
		try:    result[i+j]=plus(result[i+j],multiply(a[i],b[j]))
		except: result[i+j]=multiply(a[i],b[j])
    return result

ans={0:1}
maxMults=50
for i in xrange(1,maxMults+1):
    x={0:{1:i}, 1:{0:1,1:-i}}
    ans=multiply(ans,x)
print ans[20]

