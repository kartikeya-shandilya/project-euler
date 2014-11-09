#!/usr/bin/python

chlist=("|","B","W")
blim=60
wlim=40

for i in range (1,100000):
 total=""
 prev="|"
 cb=0
 cw=0
 while (cb<blim or cw<wlim):
  import random
  ran=str(chlist[random.randrange(0, 3)])
  if ((ran == "|" and prev != "|")or(ran == "B" and cb<blim)or(ran == "W" and cw<wlim)):
   total=total+ran
   prev=ran
   if ran=="B":
    cb=cb+1
   if ran=="W":
    cw=cw+1
 line=total.split("|")
 curr=""
 for elm in line:
  temp=""
  for char in elm:
   temp=temp+str(char)+","
#  print ":",len(temp),len(temp)-1
  temp=temp[0:len(temp)-1]
  elm=temp.split(",")
  elm.sort()
  curr=curr+str(elm)+","
 curr=curr[0:len(curr)-1]
 ans=curr.split(",")
 ans.sort()
 print ans
