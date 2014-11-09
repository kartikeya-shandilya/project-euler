
All_x=[-1,1,1]
All_y=[0,-2,2]

small=[]
large=[]

for i in xrange(3):
	x=All_x[i]
	y=All_y[i]
	while 1:
		x_new=-2*x-y-1
		y_new=-3*x-2*y-1
		x=x_new
		y=y_new
		p=3*x-1
		if p>10**9:	break
		elif x>1:
			if p not in small: small.append(p)

All_x=[1,-1,-1]
All_y=[0,-2,2]

for i in xrange(3):
	x=All_x[i]
	y=All_y[i]
	while 1:
		x_new=-2*x-y+1
		y_new=-3*x-2*y+1
		x=x_new
		y=y_new
		p=3*x+1
		if p>10**9:	break
		elif x>1:
			if p not in large: large.append(p)

sum(small)+sum(large)
#518408346
