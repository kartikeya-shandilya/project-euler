
def mult(a,b):
 c=[]
 for k in range(0,len(a)+len(b)-1):
  c.append([0,0])
 for i in range(0,len(a)):
  for j in range(0,len(b)):
   c[i+j][0]+=a[i][0]*b[j][0]
   c[i+j][1]+=a[i][1]*b[j][1]
 return c

a=[[1,1],[0,1]]
x=[[1,1]]

for i in range(1,2):
 x=mult(x,a)

