#!/usr/bin/python

f=open('/public/skartik/training/perl/pe/python/base_exp.txt','r')
max=0
cnt=0
for line in f:
 line=line.strip()
 div=line.split(",")
# print div[0]
 cnt=cnt+1
 from math import log
 val=float(div[1])*log(float(div[0]))
 if val>max:
  max=val
  ans=cnt

f.close()

print ans
