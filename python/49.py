#!/usr/bin/python

list=[]
for n in range(1000,10000):
 div=0
 if n%2==0:
  div=1
 from math import sqrt
 for j in range(3,1+int(sqrt(n))):
  if n%j==0:
   div=1
   break
  j+=2
 if div==0:
  l=[]
  for k in str(n):
   l.append(k)
  m=['|']
  m.append(n)
  l.sort()
  list.append(l+m)
#  print list

list.sort()
final=[]
prev=[]
temp=[]
for i in list:
# print "_",i,"_",i[:len(i)-2],"_",prev
 if i[:len(i)-2]==prev:
#  print "match"
  temp.append(i[-1])
 else:
  if temp!="":
   final.append(temp)
  temp=[]
  temp.append(i[-1])
 prev=i[:len(i)-2]

final.append(temp)

for i in final:
 if len(i)>2:
#  print "check:",i
  for a in i:
   for b in i:
    if a!=b:
     try:
#      print "for",a,b,"find",str((int(a)+int(b))/2)
      if i.index((int(a)+int(b))/2):
        print "the ans is :",a,b,(int(a)+int(b))/2
     except:
      b=b
