#!/usr/bin/python


def funk(n):
 if n<=2:
  return 1
# if n==3:
#  return 2
# if n==4:
#  return 4
 j=funk(n-1)
 for i in range (-1,n-3):
  j=j+funk(i)
 return j
#for i in range(1,8):
#print 7,funk(7)


# optimized :
'''
arr=[1,1,1]
for i in range(3,52):
 j=arr[-1]
 for k in range(0,i-3):
  j=j+arr[k]
 print i-1,j
 arr.append(j)
'''

# generalized:

arr=[0]
for i in range(1,100000):
 n=i-1
 if n<=0:
  j=1
 else:
  j=arr[n]
 for k in range(0,i-50):
  if k<=0:
   t=1
  else:
   t=arr[k]
  j=j+t
 print i-1,j
 if j>1000000:
  break
 arr.append(j)

