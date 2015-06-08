#!/usr/bin/python

# generalized:

arr1=[0,1,2,3,5]
arr2=[0,1,1,2,3]
arr3=[0,1,1,1,2]
for i in range(5,51):
 m=i-1
 n=i-2
 o=i-3
 p=i-4
 j=arr1[m]+arr1[n]
 k=arr2[m]+arr2[o]
 l=arr3[m]+arr3[p]
 print i,j+k+l-3
 arr1.append(j)
 arr2.append(k)
 arr3.append(l)

