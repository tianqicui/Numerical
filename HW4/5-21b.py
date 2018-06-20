#b)
from math import sqrt,pi
from numpy import empty
from pylab import imshow,show,hot,title,xlabel,ylabel,axis,xlim,ylim,subplot
import numpy as np
import matplotlib.pyplot as plt

q = 1.602e-19
epsilon = 8.85e-12
const = q/(4*pi*epsilon)

spacing = 1.0
side = 100.0
points = 101
separation = 10.0

# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the potentials and intensities
phi = empty([points,points],float)
Ex = empty([points,points],float)
Ey = empty([points,points],float)
E = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*(i-1)
    for j in range(points):
        x = spacing*(j-1)
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        if i == 51 and j == 46:
            phi[i,j] = -10*100*const
        elif i == 51 and  j == 56:
            phi[i,j] = 10*100*const
        else:
            phi[i,j] = 100*const*(1/r1-1/r2)

for i in range(points-1):
    for j in range(points-1):
        Ex[i,j] = (phi[i+1,j] - phi[i-1,j])/(2*spacing)
        Ey[i,j] = (phi[i,j+1] - phi[i,j-1])/(2*spacing)
        E[i,j] = sqrt((Ex[i,j])**2 + (Ey[i,j])**2)

#Make the plot of magnitude of electrical fields
title('Electric field on a 1m × 1m square plane')
xlabel('x/cm')
ylabel('y/cm')
imshow(E,vmax=const,vmin=-const,origin="lower",extent=[0,side,0,side])
show()

x,y = np.meshgrid(np.arange(0, 101), np.arange(0, 101))
Ex = -const*((x-x1)/((x-x1)**2+(y-y1)**2)**1.5 - (x-x2)/((x-x2)**2+(y-y2)**2)**1.5)
Ey = -const*((y-y1)/((x-x1)**2+(y-y1)**2)**1.5 - (y-y2)/((x-x2)**2+(y-y2)**2)**1.5)

#Make the plot of directions of electrical fields
title('Electric field on a 1m × 1m square plane')
xlabel('x/cm')
ylabel('y/cm')
axis([0.0,100.0,0.0,100.0])
plt.axes().set_aspect('equal')
plt.streamplot(x,y,Ex,Ey)
show()