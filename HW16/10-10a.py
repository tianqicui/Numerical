# Exercise 10.10
#a)
from numpy.random import standard_normal
from random import random
import numpy as np
from pylab import plot,title,xlabel,ylabel,show

# Definition of f(x)
def f(x):
    return x**2 - np.cos(4*np.pi*x)

# Input temperature profiles and initial values
Tmax = 1
Tmin = 1e-5
tau = 1e4
x = 2
xplot = [x]
soln = f(x)
t = 0
T = Tmax

# Simulated annealing algorithm
while T>Tmin:
    t += 1
    T = Tmax*np.exp(-t/tau)
    old_soln = soln
    dx = standard_normal()
    x += dx
    soln = f(x)
    delta = soln - old_soln
    if random()>np.exp(-delta/T):
        x -= dx
        soln = old_soln
        xplot.append(x)

# Plot the values of x as a function of time during the run
plot(xplot,'.')
xlabel("time")
ylabel("x")
title("Values of x as a function of time during the run")
show()

# From the plot we could find that the global minimum appears at around x = 0, which confirms our observation.