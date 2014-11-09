#!/usr/bin/python

i=0

while i>=0:

 for k in range(1,100):
  for j in range(k,100):
   for m in range(1,100):
    for l in range(m,100):
 
     a=j**2-k**2
     b=2*j*k
     c=l**2-m**2
     d=2*l*m
     X=(a**2+b**2)*(c**2+d**2)
     Y=2*a*b*(c**2+d**2)
     Z=2*c*d*(a**2+b**2)
 
     if Y>Z:
 #     print Y-Z
      from math import sqrt
      if sqrt(Y+Z)==int(sqrt(Y+Z)):
       i=i+1
       print "Y+Z fine",k,j,m,l
       from math import sqrt
 #      print sqrt(Y-Z)
       if sqrt(Y-Z)==int(sqrt(Y-Z)):
        print "Y-Z fine\n"
        i=-100;
        print "j=",j,"k=",k,"l=",l,"m=",m,"\n"
        print "a=",a,"b=",b,"c=",c,"d=",d,"\n"
        print "x=",X,"y=",Y,"z=",Z,"\n\n"

