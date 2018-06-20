#b)
from math import sin, cos, pi, sqrt
from numpy import empty
from pylab import imshow, gray, hot

def f(m, x, theta):
    return cos(m*theta-x*sin(theta))/pi

N = 1000
a = 0
b = pi
h = (b-a)/N

def J(m, x):
    s = f(m, x, a) + f(m, x, b)
    for i in range(1, N):
        theta = a + i * h
        if i % 2 == 1:
            s += 4 * f(m, x, theta)
        else:
            s += 2 * f(m, x, theta)
    return (s*h/3)

l = 500
k = 2*pi/l
side = 2000.0
spacing = 10.0
points = 201
xc = side/2
yc = side/2

I = empty([points,points],float)

for i in range(points):
    y = spacing*(i-1)
    for j in range(points):
        x = spacing*(j-1)
        r = sqrt((x-xc)**2+(y-yc)**2)
        if i == 101 and j == 101:
            I[i,j] = 1/4
        else:
            I[i,j] = (J(1,k*r)/(k*r))**2

imshow(I,vmax = 0.01, origin="lower",extent=[0,side,0,side])
hot()
show()