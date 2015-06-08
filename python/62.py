#!/usr/bin/python

def permutate(seq):
 if not seq:
  return [seq] # is an empty sequence
 else:
  temp = []
  for k in range(len(seq)):
   part = seq[:k] + seq[k+1:]
   for m in permutate(part):
    l=seq[k:k+1] + m
    try:
     if temp.index(l):
      k=k
    except:
     if l[0]!="0" or len(l)!=5:
      temp.append(l)
  return temp

list=[]
list=permutate('41063625')
print "permutation of 41063625 :\n",list

'''
for i in range(10,100):
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
    if k[0]!="0":
     this.append(k)
     cnt+=1
# print "no good :",i,j,cnt,this
 if cnt>=2:
  print "gr8 :",i,j,this
# else :
#  print "no good :",i,j,cnt
'''
