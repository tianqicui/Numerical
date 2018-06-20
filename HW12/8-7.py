# Exercise 8.7
#b)
from pylab import plot,show,legend,figure,xlabel,ylabel,title,axis,figure
from numpy import arange,array,sin,cos,pi,sqrt,where

# Definition of four first-order equations
def f(r,t,m):
    # Input the function vector
    x,y,vx,vy = r
    # Input constants
    C = 0.47
    R = 0.08
    density = 1.22
    g = 9.81
    alpha = pi*R**2*density*C/(2*m)
    # Calculate the derivatives
    fx = vx
    fy = vy
    fxx = -alpha*vx*sqrt(vx**2 + vy**2)
    fyy = -g-alpha*vy*sqrt(vx**2 + vy**2) 
    return array([fx,fy,fxx,fyy],float)

# Algorithms of Runge-Kutta method
def RK4(f,a,b,N,m):
    # Input range and interval of time
    h = (b-a)/N
    time = arange(a,b,h,float)
    # Make arrays to store the results
    xsoln = []
    ysoln = []
    # Input initial position and velocity
    angle = pi/6
    v0 = 100
    vx = v0*cos(angle)
    vy = v0*sin(angle)
    r = array([0,0,vx,vy],float)
    # Calculate position and velocity at any time by Runge-Kutta method
    for t in time:
        x,y,vx,vy = r
        xsoln.append(x)
        ysoln.append(y)
        k1 = h*f(r,t,m)
        k2 = h*f(r + 0.5*k1,t + 0.5*h,m)
        k3 = h*f(r + 0.5*k2,t + 0.5*h,m)
        k4 = h*f(r + k3,t + h,m)
        r += (k1 + 2*(k2+k3) + k4)/6
    plot(xsoln,ysoln,label='m = %s kg'%(m))
    return xsoln,ysoln

# Input range and interval of time
a = 0.0
b = 10
N = 10000

# Make the plot of trajectory for cannonball with m = 1 kg
figure(1)
m = 1
x,y = RK4(f,a,b,N,m)
plot(x,y)
xlabel("x/m")
ylabel("y/m")
title("Trajectory for cannonball with m = 1 kg")
legend(loc='best')
axis([0,300,0,60])

#c)
# Make the plot of trajectories for cannonball with different masses
figure(2)
masses = array([0.1,0.2,0.5,1,2,5,10])
solns = [RK4(f,a,b,N,m) for m in masses]
xlabel("x/m")
ylabel("y/m")
title("Trajectories for cannonballs with different masses")
axis([0,900,0,120])
legend(loc='best')
show()

# From the plot we find that when considering air resistance, a greater mass will cause a longer travel distance.
# Thus, mass will certainly make a difference if an object is flying through the air in real life.