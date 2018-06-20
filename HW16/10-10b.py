#b)
from numpy.random import standard_normal
from random import random
import numpy as np
from pylab import plot,title,xlabel,ylabel,show

# Definition of f(x)
def f(x):
    return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)

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
    if random()>np.exp(-delta/T) or x>50 or x<0:
        x -= dx
        soln = old_soln
        xplot.append(x)

# Plot the values of x as a function of time during the run
plot(xplot,'.')
xlabel("time")
ylabel("x")
title("Values of x as a function of time during the run")
show()

# After run for several times, we find that the minimum may appear at around x = 16, x = 2 or x = 42, which is in accord with the hint.