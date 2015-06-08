#!/usr/bin/python

mat=[]

for n in range(0,10):
 mat.append([])
 k=n
 print n
 while (k>=0):
  if(k==n):
   print "if"
   mat[n].append(1)
  else:
   print "else"
   mat[n].insert(0,(mat[n-k][k]+mat[n][k+1]))
  print k,"=",mat[n][k]
  k=k-1
 print


# here n,k     actually is  n,n-k
#      n,k = n-k,k + n,k+1    therefore =>  k,n-k + n,k-1
