
import math

init=15
r=5
for x in range(1,16):
	y=int(init*r)+10
	while y<init*5.9:
		i=int((math.sqrt(2)*y))
		print x,y,i,r
		if 2*y*(y-1)==i*(i-1):
			print y,i
			r=y/(init*1.0)
			init=y
			break
		y+=1

