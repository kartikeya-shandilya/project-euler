
from sympy import Symbol, acos, sin, pi, sqrt, cot, integrate

x = Symbol("x")
r = Symbol("r")
H = Symbol("H")
a = Symbol("a")

#ans = (H**2)*((x**2+H**2-r**2)/(2*H*x))*sqrt(1-((x**2+H**2-r**2)/(2*H*x))**2)

ans = pi*(H**2)
ans = ans - (pi/90)*acos((x**2+H**2-r**2)/(2*H*x))*(H**2) + (H**2)*((x**2+H**2-r**2)/(2*H*x))*sqrt(1-((x**2+H**2-r**2)/(2*H*x))**2)
ans = ans - (pi/90)*acos((r**2+x**2-H**2)/(2*r*x))*(r**2) + (r**2)*((r**2+x**2-H**2)/(2*r*x))*sqrt(1-((r**2+x**2-H**2)/(2*r*x))**2)

print ans
print

print integrate(ans, (H,(r-x)*(cot(a))**2,(r+x)*(cot(a))**2))
print


