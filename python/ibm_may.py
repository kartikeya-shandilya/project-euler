
import math

for i in xrange(24):
	if int(`i`[-1])<6:
		if i<10:	x="0"+`i`
		else:		x=`i`
		for j in xrange(6):
			digtime = x+":"+`j`+`j`+":"+x[::-1]
			digarr = digtime.split(":")
			hh = int(digarr[0])
			mm = int(digarr[1])
			ss = int(digarr[2])
			
			hhangle = (hh%12 + mm/60.0 + ss/3600.0)*(180/6.0)
			mmangle = (mm + ss/60.0)*(180/30.0)
			
			ssangle = (ss)*(180/30.0)
			
			if abs((ssangle - hhangle)-(ssangle - mmangle)) < 10:
				print digtime, (ssangle - hhangle), (ssangle - mmangle)