
def make_zdd(trial, _cows):
	_zdd = {}
	_zdd["T"] = [None, "T", "T"]
	_zdd["F"] = [None, "F", "F"]
	_trial = [`x` + "_" + trial[x] for x in xrange(len(trial))]
	_tria1 = [trial[x] for x in xrange(len(trial))]
	for i in xrange(len(_trial)):
		for j in xrange(max(0,_cows-i), _cows+1):
			if i != len(_trial)-1:
				if j == 0:
					_zdd[str(_trial[i])+"_"+str(j)] = [_tria1[i], str(_trial[i+1])+"_0", "F"]
				elif j == 1:
					_zdd[str(_trial[i])+"_"+str(j)] = [_tria1[i], str(_trial[i+1])+"_"+str(j), "T"]
				else:
					_zdd[str(_trial[i])+"_"+str(j)] = [_tria1[i], str(_trial[i+1])+"_"+str(j), str(_trial[i+1])+"_"+str(j-1)]
			else:
				if j == 1:
					_zdd[str(_trial[i])+"_"+str(j)] = [_tria1[i], "F", "T"]
				else:
					_zdd[str(_trial[i])+"_"+str(j)] = [_tria1[i], "T", "F"]
	return _zdd

def meld_zdd(n1, zdd1, n2, zdd2, zdd={}):
	ans = ""
	if zdd1[n1][0] in ["T", "F"] or zdd1[n2][0] in ["T", "F"]:
		return ""
	if zdd1[n1][0] == zdd2[n2][0]:
		lo = meld_zdd(zdd1[n1][1], zdd1, zdd2[n2][1], zdd2, zdd)
		hi = meld_zdd(zdd1[n1][2], zdd1, zdd2[n2][2], zdd2, zdd)
		zdd[n1] = [zdd1[n1][0], lo, hi]
		ans = n1
	elif zdd1[n1][0] < zdd2[n2][0]:
		lo = meld_zdd(zdd1[n1][1], zdd1, n2, zdd2, zdd)
		hi = zdd1[n1][2]
		zdd[n1] = [zdd1[n1][0], lo, hi]
		ans = n1
	elif zdd1[n1][0] > zdd2[n2][0]:
		lo = meld_zdd(n1, zdd1, zdd2[n2][1], zdd2, zdd)
		hi = zdd2[n2][2]
		zdd[n1] = [zdd2[n2][0], lo, hi]
		ans = n2
	else:
		zdd["tmp"] = ["tmp", "tmp", "tmp"]
		ans = "tmp"
	return ans
	
	

z1 = make_zdd("90342",2)
z2 = make_zdd("70794",0)
#z1 = make_zdd("90342",2)
print "\nz1:"
for key in z1:
	print key, "::", z1[key]
print "\nz2:"
for key in z2:
	print key, "::", z2[key]	
	
zdd={}
meld_zdd("0_9_2", z1, "0_7_0", z2, zdd)
print "\nzdd:"
for key in zdd:
	print key, "::", zdd[key]	

