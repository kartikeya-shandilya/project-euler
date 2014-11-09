
f=open("./allroots2.txt","r")

def summ(arr):
	ans=int(arr[0:1])
	for el in xrange(99):
		ans=ans+int(arr[el+2:el+3])
	return ans

sum=0;i=2;
for line in f.readlines():
	this=summ(line)
	print i,line,this
	i=i+1
	sum=sum+this

print sum
