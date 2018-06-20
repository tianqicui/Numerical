#Exercise 6.18
#a)
from numpy import *
from pylab import *

# Gaussian integration method
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

# Definition of functions
def func(x):
    return x**3 / (exp(x) - 1)

def eta(f,x,w,gamma1,gamma2,T):
    N = 100
    s = 0.0
    xp = 0.5*(x*(gamma1-gamma2)/T + (gamma1+gamma2)/T)
    wp = 0.5*w*(gamma1-gamma2)/T
    for i in range(N):
        s += 15/(pi**4)*f(xp[i])*wp[i]
    return s

# Values of physical constants
c = 2.99792458e8
h = 6.62607004e-34
k = 1.38064852e-23

# Upper bound and lower bound of integrals   
wav1 = 390e-9
wav2 = 750e-9
gamma1 = h*c/(k*wav1)
gamma2 = h*c/(k*wav2)

# Sample points and weights for Gaussian integration
N = 100
x,w = gaussxw(N)
T = arange(300,10000,1)
efficiency = [eta(func,x,w,gamma1,gamma2,Tn) for Tn in T]

# Make a graph for efficiency as function of temperature
plot(T,efficiency)
xlabel('Temperature/K')
ylabel('Efficiency')
axis([300,10000,0,1])
title('Efficiency as a function of temperature')
grid(True)
show()

#b)
# Algorithm of golden ratio search
def grs(f,x1,x4,epsilon):
    z = (1 + sqrt(5))/2
    #Calculate interior values based on Golden ratio
    x2 = x4 - (x4 - x1)/z
    x3 = x1 + (x4 - x1)/z
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)
    while True:
        if f2 < f3:
            x4 = x3
            f4 = f3
            x3 = x2
            f3 = f2
            x2 = x4 - (x4 - x1)/z
            f2 = f(x2)
        else:
            x1 = x2
            f1 = f2
            x2 = x3
            f2 = f3
            x3 = x1 + (x4 - x1)/z
            f3 = f(x3)
        if abs(x4-x1) < epsilon:
            x2 = (x1 + x4)/2
            break
    return x2, -f(x2)

# Maximum of a function f(x) could be calculated by the minimum of -f(x)
def minus_eta(T):
    return -eta(func,x,w,gamma1,gamma2,T)

x1,x4 = 300,10000
error = 1e-6
max = grs(minus_eta,x1,x4,error)
print(max)

# By this method we find that maximun efficiency appears at T=6928.5793160654539K, with a value of 0.45169384029450593.
# The results are in accordance with the plot we got in part a).

#c)
# We find the value of temperature is approximate 6929K, which is much hogher than melting point(3695K) and boiling point(5933K) of tungsten.
# So we could indicate that it is not practical to run a tungsten-filament light bulb at the temperature.