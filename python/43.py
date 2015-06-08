#!/usr/bin/python

def permutate(seq):
 if not seq:
  return [seq] # is an empty sequence
 else:
  temp = []
  for k in range(len(seq)):
   part = seq[:k] + seq[k+1:]
   for m in permutate(part):
    temp.append(seq[k:k+1] + m)
  return temp

prime=[2,3,5,7,11,13,17]

list=permutate('0123456789')
list.sort()
#list=['1406357289','3572891406']
print len(list)

sum=0
for i in list:
 if int(i) > 1000000000:
  tag=0
  j=0
  while j<7:
#   print "check",i,j,int(i[1+j:(4+j)]),prime[j],int(i[1+j:(4+j)])%prime[j]
   if int(i[1+j:4+j])%prime[j]>0:
    tag=1
    break
   j+=1
  if tag==0:
   sum=sum+int(i)
   print i,sum
