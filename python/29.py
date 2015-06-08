#!usr/bin/python

arr=[]
for a in range(2,101):
 for b in range(2,101):
  arr.append(a**b)

arr.sort()
count=1

for i in range(0,len(arr)-1):
 if arr[i]!=arr[i+1]:
  count=count+1

print count
