#!/usr/bin/python

ten=0
for i in range(1,1000):
 ten=(ten+(i**i)%10000000000)%10000000000

print ten
