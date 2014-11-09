#!/usr/bin/python

#list=[2,5,10,50,100,200]
list=[2,5]


arr=[0]
cur=[0]
for i in range(0,201):
 arr.append(1)
 cur.append(0)
for i in list:
 for j in range(1,201):
  k=j
  while k>0:
   cur[j]=cur[j]+arr[k]
   k=k-i
  cur[j]=cur[j]+int(j/i)
 for k in range(1,j+1):
  arr[k]=cur[k]
  cur[k]=0

print arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10]
print arr[11],arr[12],arr[13],arr[14],arr[15],arr[16],arr[17],arr[18],arr[19],arr[20]
print arr[200]
print

'''
arr=[0]
cur=[0]
for i in range(1,201):
 arr.append(1)
 cur.append(0)
for j in range(1,201):
 for i in list:
  k=j
  while k>0:
   cur[j]=cur[j]+arr[k]
   k=k-i
  cur[j]=cur[j]+int(j/i)
 for k in range(1,j+1):
  arr[k]=cur[k]
  cur[k]=0
print arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10]
print arr[11],arr[12],arr[13],arr[14],arr[15],arr[16],arr[17],arr[18],arr[19],arr[20]
print arr[200]
'''
