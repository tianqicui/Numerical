#c)
from numpy import sin,pi,linspace
from pylab import *

#Gaussian integration method
def gaussxw(N):
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    return x,w

q0 = 10*1.602e-19
epsilon0 = 8.85e-12
const = 1/(4*pi*epsilon0)
spacing = 1.0
side = 100.0
points = 101
L = 10
sigma = lambda x,y: q0*sin(2*pi*x/L)*sin(2*pi*y/L)

N = 10
x,w = gaussxw(N)
a = -L/2
b = L/2
xp = 0.5*(b-a)*x + 0.5*(b+a)
yp = xp	
wp = 0.5*(b-a)*w

#Calculate the potential in the array
def phi_f(x_,y_):
    s=0
    for i,xi in enumerate(xp):
        for j,yj in enumerate(yp):
            r = sqrt((x_-xi)**2 + (y_-yj)**2)
            if r > 1e-6:
                dphi = sigma(xi,yj)/r
            else:
                dphi = 0
            s+=const*wp[i]*wp[j]*dphi
    return s

# Make an array to store the potentials and intensities
phi = empty([points,points],float)
Ex = empty([points,points],float)
Ey = empty([points,points],float)
E = empty([points,points],float)
direction = empty([points,points],float)

# Calculate the values in the array
for i,xi in enumerate(arange(-side/2,side/2,spacing)):
    for j,yj in enumerate(arange(-side/2,side/2,spacing)):
        phi[i,j] = phi_f(xi,yj)

for i in range(points-1):
    for j in range(points-1):
        Ex[i,j] = (phi[i+1,j] - phi[i-1,j])/(2*spacing)
        Ey[i,j] = (phi[i,j+1] - phi[i,j-1])/(2*spacing)
        E[i,j] = sqrt((Ex[i,j])**2 + (Ey[i,j])**2)
        direction[i,j] = angle(Ex[i,j] + 1j*Ey[i,j])

#Make the plot of magnitude of electrical fields
title('Electric field on a 1m × 1m square plane')
xlabel('x/cm')
ylabel('y/cm')
imshow(E,origin="lower",extent=[0,side,0,side])
show()

#Make the plot of directions of electrical fields
hsv()
title('Electric field on a 1m × 1m square plane')
xlabel('x/cm')
ylabel('y/cm')
imshow(direction,origin="lower",extent=[0,side,0,side])
show()