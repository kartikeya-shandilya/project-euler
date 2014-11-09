#!/usr/bin/python

fac=[]
for i in range(0,10):
 prod=1
 j=i
 while j>1:
  prod=prod*j
  j-=1
 fac.append(prod)

ans=0
for i in range(1,1000000):
 if i%10000==0:
  print i
 temp=[]
 temp.append(i)
 flag=1
 while flag==1:
  new=0
  last=str(temp[-1])
  for j in range(0,len(last)):
   new=new+fac[int(last[int(j)])]
  try:
   if temp.index(new)>=0:
    temp.append(new)
    flag=0
  except:
   temp.append(new)
 if len(temp)>60:
  ans+=1
#  print i,temp,len(temp)

print ans

