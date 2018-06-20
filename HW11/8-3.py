#Exercise 8.3
#a)
from numpy import array,arange
from pylab import plot,xlabel,ylabel,title,figure,show

# Input value of constants in equations
sigma_const = 10
r_const = 28
b_const = 8/3

# Definition of Lorenz equations
def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = r_const*x - y - x*z
    fz = x*y - b_const*z
    return array([fx,fy,fz],float)

# Input range and interval of time
left = 0.0
right = 50.0
N = 10000
h = (right-left)/N

# Make arrays to store the results
tpoints = arange(left,right,h)
xpoints = []
ypoints = []
zpoints = []

# Input initial conditions
r = array([0,1,0],float)

# Use Runge–Kutta method to solve equations
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])				
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

# Make the plot of y as function of t
figure(1)
plot(tpoints,ypoints)
xlabel("t")
ylabel("y")
title("y vs t")
show()

# From figure 1 we notice that it is quite hard to tract the trajectory of y. 

#b)
# Make the plot of z as function of x
figure(2)
plot(zpoints,xpoints)
xlabel("x")
ylabel("z")
title("z vs x")
show()

# From figure 2 we notice that the trajectory of z and x has the similar shape of butterfly if we ingore the initial part.