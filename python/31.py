#!/usr/bin/python

count=0

for a in range(0,201):
# print "a =",a
 for b in range(0,min(101,int((202-a)/2))):
#  print "b =",b
  for c in range(0,min(41,int((205-a-2*b)/5))):
#   print "c =",c
   for d in range(0,min(21,int(210-a-2*b-5*c)/10)):
    for e in range(0,min(11,int(220-a-2*b-5*c-10*d)/20)):
     for f in range(0,min(6,int(250-a-2*b-5*c-10*d-20*e)/50)):
      for g in range(0,min(3,int(300-a-2*b-5*c-10*d-20*e-50*f)/100)):
       for h in range(0,min(2,int(400-a-2*b-5*c-10*d-20*e-50*f-100*g)/200)):
#   d=0
#   e=0
#   f=0
#   g=0
#   h=0
#       print "a+b+c =",a+b+c
        if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h==200:
         count=count+1
         print count

print "ans =",count
