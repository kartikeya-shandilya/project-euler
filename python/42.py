#!/usr/bin/python

f=open('42.txt','r')

val=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

line=f.readline()
words=line.split(",")

count=0
#print val.index(str("W"))
#print val.index(str("F"))

for temp in words:
 if temp != "":
  sum=0
  for i in range (0,len(temp)):
#   print temp,temp[i]
   sum=sum+1+val.index(str(temp[i]))
#   print sum
  from math import sqrt
  if int(sqrt(1+8*sum))==sqrt(1+8*sum):
   count=count+1
  print count
