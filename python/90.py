
global sqlist
sqlist=["01","04","09","16","25","36","49","64","81"]

def allsq(cub1,cub2):
	global sqlist
	res=1
	for elm in sqlist:
		if elm[0] in cub1 and elm[1] in cub2:
			continue
		elif elm[0] in cub2 and elm[1] in cub1:
			continue
		else:
			res=0
			break
	return res

def extend(cube):
	if "6" in cube:
		if "9" not in cube:
			cube.append("9")
	if "9" in cube:
		if "6" not in cube:
			cube.append("6")
	return cube

allremovals=[]

for i in xrange(10):
	for j in xrange(i+1,10):
		for k in xrange(j+1,10):
			for l in xrange(k+1,10):
				newlist=[`i`,`j`,`k`,`l`]
				allremovals.append(newlist)

allposs=["0","1","2","3","4","5","6","7","8","9"]
allcube=[]

for rem in allremovals:
	newcube=allposs[:]
	for elm in rem:
		newcube.remove(elm)
	allcube.append(newcube)

cnt=0
for i in xrange(210):
	for j in xrange(i+1,210):
		cnt=cnt+allsq(extend(allcube[i]),extend(allcube[j]))

print cnt