#!/usr/bin/python

ini=285
val=285
pow=10
for i in range(2,21):
 val=10*val+pow*ini
 pow*=10
 print i,"-",val
