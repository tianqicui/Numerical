# Exercise 9.4
from pylab import *

# Input constants
A = 10
B = 12
tau = 365
D = 0.1

# Thickness of crust in meters
L = 20
# Number of grid points
N = 100
# Grid spacing
a = L/N
# Time-step
h = 0.01
# Coordinates of depth
x = linspace(0,L,N+1)
# Arrays to storage values of temperature
T = zeros(N+1,float)
T[1:N]=10

# Input boundary conditions
def T0(t):
    return A + B*sin(2*pi*t/tau)

# Main loop
def iterate(T,t_min,t_max):
    t = t_min
    c = h*D/a**2
    while t<t_max:
        # Input boundary conditions
        T[0] = T0(t)
        T[N] = 11
        # Calculate temperature for each grid points
        T[1:N] = T[1:N] + c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
        t += h
    return T

# Temperature profile of the crust during the first 9 years
figure(1)
t_min = 0
for t_max in [365*(i+1) for i in range(9)]:
    T = iterate(T,t_min,t_max)
    plot(x,T,label='t = %d years'%(t_max//365))
    t_min = t_max    
legend()
xlabel("x/m")
ylabel("T/℃")
title("Temperature profile of the crust during the first 9 years")
show()

# Temperature profile of the crust in the 10th year
figure(2)
T9 = iterate(T,0,365*9)
T9_i = T9
t_min = 365*9
for t_max in [365*9 + (i+1)*(365//4) for i in range(4)]:
    #t_max = t_min + 365//4
    T9_i = iterate(T9_i,t_min,t_max)
    plot(x,T9_i,label='t = 9 years and %d months'%(3*(t_max-365*9)//(365//4)))
    t_min = t_max
legend()
xlabel("x/m")
ylabel("T/℃")
title("Temperature profile of the crust in the 10th year")
show()

# If time fixed, temperature will change towards the constant but not monotonously as the depth increased.
# If depth fixed, temperature will change periodically as the time increased.