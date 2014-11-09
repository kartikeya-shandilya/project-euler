
def getNextRand():
	s = 290797
	while 1:
		sn = s*s % 50515093
		yield (sn % 2000) - 1000
		s = sn

c = 0
for i in getNextRand():
	c += 1
	print i
	if c==1000: break

