
datedict={}

#start= [1,1,1]
start = [31,12,7]

mnths= [31,29,31,30,31,30,31,31,30,31,30,31]
flag=1

for j in range(12):
	for i in range(mnths[j]):
		for k in range(7):
			datedict[str([i+1,j+1,k+1])]=""
#print datedict

def dates(x,y,z,l):
	for i in range(1,x+1):
		datedict[str([i,y,z])]=l
	for i in range(1,y+1):
		datedict[str([x,i,z])]=l
	for i in range(1,z+1):
		datedict[str([x,y,i])]=l

while flag:
	


		
