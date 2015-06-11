#!/usr/bin/python
f=open('102.txt','r')

mat=[]
count=0
for i in range(0,1000):
 line=f.readline()
 elm=str(line).split(",")
 mat.append([])
 for j in range(0,6):
  mat[i].append(elm[j])
 x1=int(mat[i][0])
 x2=int(mat[i][2])
 x3=int(mat[i][4])
 y1=int(mat[i][1])
 y2=int(mat[i][3])
 y3=int(mat[i][5])
 c1=((y3-y1)*(x2-x1)-(x3-x1)*(y2-y1))*(-y1*(x2-x1)+x1*(y2-y1))
 c2=((y1-y2)*(x3-x2)-(x1-x2)*(y3-y2))*(-y2*(x3-x2)+x2*(y3-y2))
 c3=((y2-y1)*(x1-x3)-(x2-x1)*(y1-y3))*(-y1*(x1-x3)+x1*(y1-y3))
 if c1>0 and c2>0 and c3>0:
  count+=1

print count
