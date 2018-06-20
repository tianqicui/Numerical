#Exercise 5.21
#a)
from math import sqrt,pi
from numpy import empty
from pylab import imshow,show,hot,title,xlabel,ylabel

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

# Make an array to store the potentials
phi = empty([points,points],float)

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

# Make the plot
title('Electric potential on a 1m × 1m square plane')
xlabel('x/cm')
ylabel('y/cm')
imshow(phi,vmax=10*const, vmin=-10*const,origin="lower",extent=[0,side,0,side])
hot()
show()