#Exercise 5.4
#a)
from math import sin, cos, pi
from numpy import linspace
from pylab import plot, xlim, ylim, xlabel, ylabel, legend, title, show

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

xpoints = []
ypoints0 = []
ypoints1 = []
ypoints2 = []

for x in linspace(0,20,1000):
    xpoints.append(x)
    ypoints0.append(J(0,x))
    ypoints1.append(J(1,x))
    ypoints2.append(J(2,x))
    
xlim(0,20)
ylim(-1,1)
plot(xpoints,ypoints0,"k-",label="m=0")
plot(xpoints,ypoints1,"k--",label="m=1")
plot(xpoints,ypoints2,"ko",label="m=2")
legend(loc = 'best')
xlabel('x')
ylabel('J(m,x)')
title('Plot of Bessel functions')
show()