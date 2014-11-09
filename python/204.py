
#prim=[2,3,5]
#indx=[0]*3

prim=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
indx=[0]*25
hamm=[1]
cntr=1
flag=0

mLim=10**9+1
mLst=1

while 1:
	mMin=10**9+1
	mInd=26;
	test=[1]*25
	for i in xrange(25):
		test[i]=hamm[indx[i]]*prim[i]
		while test[i]<=mLst:
			indx[i]+=1
			test[i]=hamm[indx[i]]*prim[i]
		if test[i]<mMin and test[i]<mLim:
			mMin=test[i]
			mInd=i
	if mInd==26:	break
	hamm.append(mMin)
	indx[mInd]+=1
	mLst=mMin
	cntr+=1

print cntr
