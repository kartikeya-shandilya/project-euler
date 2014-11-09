
import sys

mat=[]
for i in range(10):
 for j in range(10):
  k=10-i-j
  if k<1:
   k=0
  mat.append(k)

m=int(sys.argv[1])

for i in range(m-1):
 old=mat
 mat=[]
 for a in range(10):
  for b in range(10):
   x=0
   if i>m-3:
    for c in range(1,10-a-b):
     x+=old[10*b+c]
   else:
    for c in range(10-a-b):
     x+=old[10*b+c]
   mat.append(x)

print mat[0]

