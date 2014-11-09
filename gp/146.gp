
#210x+10
#210x+80
#210x+130
#210x+200

n=ceil(150*10^6/(210))
sm=0
for(j=0,n,k=(210*j+10);i=k^2;if((nextprime(i+1)==(i+1)&nextprime(i+2)==(i+3)&nextprime(i+4)==(i+7)&nextprime(i+8)==(i+9)&nextprime(i+10)==(i+13)&nextprime(i+14)==(i+27)),sm+=k;print(i," ",sm)))
for(j=0,n,k=(210*j+80);i=k^2;if((nextprime(i+1)==(i+1)&nextprime(i+2)==(i+3)&nextprime(i+4)==(i+7)&nextprime(i+8)==(i+9)&nextprime(i+10)==(i+13)&nextprime(i+14)==(i+27)),sm+=k;print(i," ",sm)))
for(j=0,n,k=(210*j+130);i=k^2;if((nextprime(i+1)==(i+1)&nextprime(i+2)==(i+3)&nextprime(i+4)==(i+7)&nextprime(i+8)==(i+9)&nextprime(i+10)==(i+13)&nextprime(i+14)==(i+27)),sm+=k;print(i," ",sm)))
for(j=0,n,k=(210*j+200);i=k^2;if((nextprime(i+1)==(i+1)&nextprime(i+2)==(i+3)&nextprime(i+4)==(i+7)&nextprime(i+8)==(i+9)&nextprime(i+10)==(i+13)&nextprime(i+14)==(i+27)),sm+=k;print(i," ",sm)))

#100 10

#19595985005635600 139985670

#859458784900 140912740
#280736391936100 157667930
#14297420138112400 277239750
#16930425881980900 407356720

#99483468100 407672130
#6380019256900 410198000
#66358945210000 418344100
#1545548137171600 457657560
#9484282305798400 555044840
#14710883251864900 676333270
