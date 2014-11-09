
lst=[]

def gcd(a,b):
 if a*b==0:
  return a+b
 elif a==b:
  return a
 else:
  return gcd(a-int(a/b)*b,b-int(b/a)*a)

'''
for i in range(1,10):
 for j in range(1,10):
  print i,j,gcd(i,j)
'''

count=0
for j in range(2,10001):
 for i in range(int(j/3),int(j/2)+1):
  if j>2*i and j<3*i and gcd(i,j)==1:
   count+=1

print count

