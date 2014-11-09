#!/usr/bin/python

chlist=("|","B","W")
import sys
blim=int(sys.argv[1])
wlim=int(sys.argv[2])
#print blim,wlim


for i in range (1,100000):
 total=""
 prev="|"
 cb=0
 cw=0
 while (cb<blim or cw<wlim):
  import random
  ran=str(chlist[random.randrange(0, 3)])
  if ((ran == "|" and prev != "|")or(ran == "B" and cb<blim)or(ran == "W" and cw<wlim)):
   if ran != "|":
    total=total+ran+","
   else:
    total=total[0:len(total)-1]+ran
   prev=ran
   if ran=="B":
    cb=cb+1
   if ran=="W":
    cw=cw+1
# print "total:",total
 line=total[0:len(total)-1].split("|")
 curr=""
 for elm in line:
  temp=elm.split(",")
  temp.sort()
  for char in temp:
   curr=curr+char
  curr=curr+"|"
 curr=curr[0:len(curr)-1]
 ans=curr.split("|")
 ans.sort()
# print "ans:",ans
 print ans
