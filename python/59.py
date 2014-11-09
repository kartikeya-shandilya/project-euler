
f=open('59.txt','r')

def bin(x):
	y=0; k=0
	while(x>0):
		y=y+(10**k)*(x%2)
		x=x/2; k+=1;
	return y

def dec(x):
	y=0
	for i in range(len(str(x))):
		y=y+(2**i)*int(str(x)[len(str(x))-i-1])
	return y

def xor(a,b):
	a=str(a)[::-1]
	b=str(b)[::-1]
	c=""
	for i in range(min(len(str(a)),len(str(b)))):
		if(int(str(a)[i])+int(str(b)[i])==1):
			c+="1"
		else:
			c+="0"
	for i in range(max(len(str(a)),len(str(b)))-min(len(str(a)),len(str(b)))):
		if   (len(str(a))>len(str(b))): c+=str(a)[len(str(b))+i]
		else                          : c+=str(b)[len(str(a))+i]
	return c[::-1]

line=f.readline()
all=str(line).split(",")
temp=0

for i in range(1201):
#	z=temp
	if   i%3==0: temp+=dec(xor(bin(int(all[i])),bin(103)))
	elif i%3==1: temp+=dec(xor(bin(int(all[i])),bin(111)))
	elif i%3==2: temp+=dec(xor(bin(int(all[i])),bin(100)))
#	print temp-z

print temp
