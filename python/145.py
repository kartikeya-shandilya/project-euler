#!/usr/bin/python

seq=["1"]
diff=["0"]
sum=["0"]
for i in range(2,1001):
 seq.append(i*(3*i-1)/2)
 diff.append(int(seq[-1])-int(seq[-2]))
 sum.append(int(seq[-1])+int(seq[-2]))
 

for j in range(0,1000):
 print seq[j],diff[j],sum[j]
