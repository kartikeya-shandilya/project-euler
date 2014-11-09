
def addit(x,y):
	if x%2 + y%2 == 0 :
		return 8
	else:
		return x+y-1
	
x=1864
for i in xrange(1865,1910):
	y=i
	x=addit(x,y)

print x

print addit(3,4)
print addit(3,5)
print addit(5,4)
print addit(6,4)
