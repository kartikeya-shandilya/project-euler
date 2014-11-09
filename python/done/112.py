#!/usr/bin/python

cnt=0
for i in range(1,2500000):
 j=str(i)
 tag1="incr"
 for k in range(0,len(j)-1):
  if j[k]>j[k+1]:
   tag1="bouncy"
   break
 tag2="decr"
 for k in range(0,len(j)-1):
  if j[k]<j[k+1]:
   tag2="bouncy"
   break
 if tag1=="bouncy" and tag2=="bouncy":
  cnt+=1
# print i,tag1,tag2
 if cnt/(1.0*i)>0.99:
  print "yes",i,cnt
  break

#print "no",i,cnt
