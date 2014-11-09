k = 13779
n = 2
q = 1

m = k*n
p = k*q

p2 = p^2
q2 = q^2

m2 = m^2
n2 = n^2

a1 = (m2+n2)*(p2+q2)
b1 = (p2+q2)*(m2-n2)
c2 = (p2+q2)*(2*m*n)
b2 = (m2+n2)*(p2-q2)
c1 = (m2+n2)*(2*p*q)
a2 = ceil(sqrt(b2^2-c2^2))

y = b1*b2
z = a1*a2
x = sqrt(y^2+z^2)

print("x ",x)
print("y ",y)
print("z ",z)

print("x+y ", x+y, " ", sqrt(x+y))
print("x+z ", x+z, " ", sqrt(x+z))
print("y+z ", y+z, " ", sqrt(y+z))
print("x-y ", x-y, " ", sqrt(x-y))
print("x-z ", x-z, " ", sqrt(x-z))
print("y-z ", y-z, " ", sqrt(y-z))

print("a1 ", a1)
print("b1 ", b1)
print("c2 ", c2)
print("b2 ", b2)
print("c1 ", c1)
print("a2 ", a2)
