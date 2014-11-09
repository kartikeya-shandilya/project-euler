
f=[1,2]
s=[1,2]

for i in xrange(2,100):
	f.append(f[i-1]+f[i-2])
	s.append(s[i-1]+s[i-2]+f[i-2]-1)

N=10**17-1
ans=0

while(N>0):
	for i in xrange(len(s)):
		if(f[i]>N):
			break
	ans+=N+s[i-1]-f[i-1]
	N-=f[i-1]

print ans

