"""
P0  0,1
P1  v,1
P2  1,v
P3  1,0

Bx = (1-t)^3*0 + 3(1-t)^2t*v + 3(1-t)t^2*1 + t^3*1
By = (1-t)^3*1 + 3(1-t)^2t*1 + 3(1-t)t^2*v + t^3*0

Bx = 3*(1-t)^2*t*v + 3*(1-t)*t^2 + t^3
By = (1-t)^3 + 3*(1-t)^2*t + 3*(1-t)*t^2*v

dx = 3*(-1+t)*(-v+t*(-2+3*v))
dy = 3*t*(-2+2*t+2*v-3*t*v)

integration gives:
area = (10 + 12 v - 3 v^2)/20 = Pi / 4
v = (12 - Sqrt[264 - 60 Pi])/6
"""

from scipy import integrate
from math import pi, sqrt

v = (12 - sqrt(264 - 60*pi))/6.0

result = integrate.quad(lambda t: sqrt((3*(t-1)*(-v+t*(-2+3*v)))*(3*(t-1)*(-v+t*(-2+3*v)))+(3*t*(-2+2*t+2*v-3*t*v))*(3*t*(-2+2*t+2*v-3*t*v))), 0, 1)[0]

ans = 100*(result - pi/2)/(pi/2)
print ans

