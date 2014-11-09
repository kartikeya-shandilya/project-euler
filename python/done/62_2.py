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

#list=[]
#list=permutate('690312')
#print "permutation of 690312 :\n",list

for i in range(10,1000):
 j=i**3
 temp=permutate(str(j))
 cnt=0
 this=[]
 for k in temp:
#  print "test :",k,int(k)**(1/3.0),int(int(k)**(1/3.0))
#  print "test :",int(k)**(1/3.0),int(int(k)**(1/3.0))+1,(int(int(k)**(1/3.0))+1)**3,k
  if (int(int(k)**(1/3.0))+1)**3==int(k):
#   print "true",
   try:
#     print "try"
     if this.index(k):
      k=k
   except:
#    print "except"
    this.append(k)
    cnt+=1
# print "no good :",i,j,cnt,this
 if cnt>=2:
  print "gr8 :",i,j,this
# else :
#  print "no good :",i,j,cnt

