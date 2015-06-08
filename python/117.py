#!/usr/bin/python

# generalized:

arr=[0,1,2,4,8]
for i in range(5,51):
 j=arr[i-1]+arr[i-2]+arr[i-3]+arr[i-4]
 print i,j
 arr.append(j)

