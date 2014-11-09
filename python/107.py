#!/usr/bin/python
f=open('/public/skartik/training/perl/pe/python/107.txt','r')

mat=[]
i=0
for i in range(0,40):
 line=f.readline()
 elm=str(line).split(",")
 mat.append([])
 for j in range(0,40):
  mat[i].append(elm[j])
start=0
for i in range(0,40):
 for j in range(i,40):
  start=start+int(mat[i][j])

conn=[0]
disc=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
stop=0
while len(disc)>0:
 min=[999,40,40]
 for i in conn:
  for j in disc:
   if 0<int(mat[i][j])<min[0]:
    min[0]=int(mat[i][j])
    min[1]=i
    min[2]=j
 conn.append(int(min[2]))
 disc.remove(int(min[2]))
 for k in conn:
  mat[j][k]=0
 stop=stop+min[0]

print "conn",conn
print "disc",disc
print "start",start
print "stop",stop
print "diff",start-stop

